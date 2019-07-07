from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .models import db
from .handlers import routes
from .handlers.inventory import inventory_api
from .handlers.merchant import merchant_api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    db.app = app
    migrate = Migrate(app, db)
    app.register_blueprint(inventory_api)
    app.register_blueprint(merchant_api)
    app.register_blueprint(routes)

    return app
