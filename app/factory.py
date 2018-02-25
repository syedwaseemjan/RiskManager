import os

from flask import Flask

from app.extensions import db
from app.utils import register_blueprints
from settings import PROJECT_ROOT


def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the RiskManager platform.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered.
                                        Defaults to `True`.
    """

    app = Flask(package_name, instance_relative_config=True,
                static_url_path='/dist',
                static_folder=os.path.join(PROJECT_ROOT, 'frontend/app/dist'))

    app.config.from_object('app.settings')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)

    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if db_uri and db_uri != "sqlite:///:memory:":
        db_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', db_uri))
        db_uri = 'sqlite:///{}'.format(db_path)
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    db.init_app(app)

    register_blueprints(app, package_name, package_path)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    return app
