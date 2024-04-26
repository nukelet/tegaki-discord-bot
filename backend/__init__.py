import os
from flask import Flask

from backend import db, api_auth, upload

import secrets

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'tegaki.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello", methods=['GET'])
    def hello():
        return "Hello, World!"
    hello()

    db.init_app(app)
    api_auth.init_app(app)

    #blueprints
    app.register_blueprint(api_auth.bp)
    app.register_blueprint(upload.bp)
    # app.add_url_rule('/', endpoint='index')

    return app
