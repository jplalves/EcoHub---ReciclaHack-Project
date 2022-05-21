from flask import Blueprint, jsonify, request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from typing import Dict, Tuple, Any, List

from app.actions.users_actions import \
    get_user_by_id, get_users, update_user, create_user, login, deleted_user

from app.models.users import User


app_users = Blueprint('users', __name__)
