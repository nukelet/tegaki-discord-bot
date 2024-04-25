from flask import request, Flask, jsonify
from markupsafe import escape

app = Flask("tegaki")

@app.route("/user/<username>")
def show_user_profile(username):
    return f"<p>User: {escape(username)}</p>"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"

@app.route("/image", methods=['POST'])
def upload():
    return f"Posted image"

