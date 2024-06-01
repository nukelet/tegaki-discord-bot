import functools

from flask import (
    Blueprint, current_app, flash, g, redirect, render_template,
    request, session, url_for
)

from backend.db import get_db
from werkzeug.exceptions import abort

import click
import secrets

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/", methods=["PUT"])
def authenticate():
    # gets user key from the request
    user_key = request.form["user_key"]
    db = get_db()

    if not user_key:
        abort(403, f"No user_key was provided")

    # verify the provided key
    result = db.execute(
        "SELECT * FROM api_auth WHERE user_key = ?",
        (user_key,)
    ).fetchone()

    if result is None:
        abort(403, f"Invalid user_key")

    # clears session cookie and replaces it with user id from db
    session.clear()
    session["user_id"] = result["user_id"]
    return ({"success": True}, 200)

@click.command("generate-api-key")
def generate_api_key():
    db = get_db()

    # generate a random 32-bit user id
    user_id = secrets.randbits(32)
    # generate a random token with 16 bytes
    user_key = secrets.token_hex(16)

    try:
        # Inserts authentication keys into DB
        db.execute(
            "INSERT INTO api_auth (user_id, user_key) VALUES (?, ?)",
            (user_id, user_key),
        )

        db.commit()
    except Exception as e:
        click.echo(f"Unable to create API key: \"{e}\"")
        return;

    click.echo(f"Your API key: {user_key}")
    click.echo(f"Your API user ID: {user_id}")

def init_app(app):
    app.cli.add_command(generate_api_key)
