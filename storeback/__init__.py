from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .models import db
from .handlers import routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    db.app = app
    migrate = Migrate(app, db)
    for route in routes:
        app.register_blueprint(route)

    return app
