from database import db, migrate
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.views.templates_views import app_views
from app.models.users import User
from app.models.garbage import Garbage
from app.models.type_of_garbage import TypeOfGarbage
from app.models.cooperative import Cooperative


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('settings')
    JWTManager(app)
    db.init_app(app)
    migrate.init_app(app, db)
    _register_blueprint(app)
    return app


def _register_blueprint(app: Flask):
    app.register_blueprint(app_views)
