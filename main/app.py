from flask import Flask

from main import commands
from main.config import ProdConfig
from main.exceptions import InvalidUsage, InvalidSchema, AuthenticationError
from main.extensions import cors, db, bcrypt, migrate, jwt
from main.views import catalog, user, article


def create_app(config_object=ProdConfig):
    """Application factory to produce application instance.

    Args:
        config_object (object): the configuration loaded from `main.config`

    """

    app = Flask(__name__)
    # Ignore trailing slash in flask route
    # https://stackoverflow.com/questions/40365390/trailing-slash-in-flask-route
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Every extensions start with flask_* will be initialized here."""

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)


def register_blueprints(app):
    """Register endpoints here.  Also do allow CORS."""

    # Allow CORS
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(catalog.blueprint, origins=origins)

    # Register all endpoints in `main.views`
    app.register_blueprint(catalog.blueprint)
    app.register_blueprint(user.blueprint)
    app.register_blueprint(article.blueprint)


def register_error_handlers(app):
    """The errors should be raised in the same format."""

    def error_handler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(InvalidUsage)(error_handler)
    app.errorhandler(InvalidSchema)(error_handler)
    app.errorhandler(AuthenticationError)(error_handler)


def register_commands(app):
    """Register all the command used by CLI"""

    app.cli.add_command(commands.test)
    app.cli.add_command(commands.urls)
