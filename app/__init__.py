from database import db, migrate
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.views.templates_views import app_views
from app.models.entities.users import User
from app.models.entities.comments import Comments
from app.models.entities.garbage import Garbage
from app.models.entities.cooperative import Cooperative


def create_app():
    app = Flask(__name__, template_folder="./templates", static_folder="./templates")
    CORS(app)
    app.config.from_object('settings')
    JWTManager(app)
    db.init_app(app)
    migrate.init_app(app, db)
    _register_blueprint(app)
    return app


def _register_blueprint(app: Flask):
    app.register_blueprint(app_views)
