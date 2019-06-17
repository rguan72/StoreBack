from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .handlers import routes
from .handlers.inventory import inventory_api

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(inventory_api)
    app.register_blueprint(routes)

    return app
