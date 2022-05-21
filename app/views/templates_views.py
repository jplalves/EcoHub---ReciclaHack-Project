import json
from app.actions.garbage_actions import get_garbage
from app.actions.cooperative_actions import login_coop
from app.actions.users_actions import create_user, login_user
from flask import Blueprint, render_template, request, redirect, Response

app_views = Blueprint('views', __name__)


# Templates
@app_views.route('/', methods=['GET'])
def home_view():
    return render_template('index.html')


@app_views.route('/how_to_recycle', methods=['GET'])
def how_to_recycle_view():
    _json = request.get_json()
    return render_template('index.html', context=_json)


@app_views.route('/where_recycle', methods=['GET'])
def where_recycle_view():
    # _json = request.get_json()
    return render_template('index.html')


@app_views.route('/login', methods=['POST', 'GET'])
def login_view():
    if request.method == 'GET':
        return render_template('login.html', status=True)

    credentials = request.values
    token = login_user(credentials.get('email'), credentials.get("password"))
    if token:
        return render_template('index.html', token=token)
    return render_template('login.html', status=False)


@app_views.route('/logout', methods=['GET'])
def logout_view():
    return redirect('/')


@app_views.route('/register', methods=['POST', 'GET'])
def register_view():
    if request.method == 'GET':
        return render_template('register.html', status=True)

    credentials = request.values
    user = create_user(credentials)
    if user:
        return render_template('index.html', user=user.serialize())
    return render_template('register.html', status=False)


@app_views.route('/tips', methods=['POST', 'GET'])
def tips_view():
    if request.method == 'GET':
        list_garbage = get_garbage()
        return render_template('tips.html', list_garbage=list_garbage)

    return render_template('tips.html')
