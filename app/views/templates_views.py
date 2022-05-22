import os
import json
from app.models.type_of_garbage import TypeOfGarbage
from app.actions.cooperative_actions import login_coop
from app.actions.users_actions import create_user, login_user
from flask import Blueprint, render_template, request, redirect
from app.actions.comments_actions import get_comment_by_garbage_id, create_comment
from app.actions.garbage_actions import get_garbage_by_id, get_garbage_by_type, create_garbage, get_garbage_by_name

app_views = Blueprint('views', __name__)


# Templates
@app_views.route('/', methods=['GET'])
def home_view():
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


@app_views.route('/tips', methods=['GET'])
def tips_view():
    if request.method == 'GET':
        _tp = TypeOfGarbage()
        list_garbage_plastic = get_garbage_by_type(type_of_garbage=_tp.plastic.get('name'))
        list_garbage_glass = get_garbage_by_type(type_of_garbage=_tp.glass.get('name'))
        list_garbage_metal = get_garbage_by_type(type_of_garbage=_tp.metal.get('name'))
        list_garbage_paper = get_garbage_by_type(type_of_garbage=_tp.paper.get('name'))
        return render_template('tips.html', list_garbage_plastic=list_garbage_plastic,
                               list_garbage_glass=list_garbage_glass,
                               list_garbage_metal=list_garbage_metal,
                               list_garbage_paper=list_garbage_paper)


@app_views.route('/tips/search/', methods=['GET'])
def tips_search_view():
    data = request.values
    list_garbage = get_garbage_by_name(garbage_name=data['garbage_name'])
    return render_template('tips_search.html', list_garbage=list_garbage)


@app_views.route('/tips/search/garbage/<garbage_id>', methods=['POST', 'GET'])
def type_search_garbage_view(garbage_id):
    garbage = get_garbage_by_id(garbage_id)
    comments = [comment.serialize() for comment in get_comment_by_garbage_id(garbage_id)]
    return render_template('garbage.html', garbage=garbage.serialize(), comments=comments)


@app_views.route('/garbage/<garbage_id>', methods=['POST', 'GET'])
def garbage_view(garbage_id):
    garbage = get_garbage_by_id(garbage_id)
    comments = [comment.serialize() for comment in get_comment_by_garbage_id(garbage_id)]
    return render_template('garbage.html', garbage=garbage.serialize(), comments=comments)


@app_views.route('/ranking', methods=['GET'])
def ranking_view():
    return render_template('ranking.html')


@app_views.route('/register/garbage', methods=['POST', 'GET'])
def register_garbage_view():
    if request.method == "GET":
        return render_template('/forms/form_garbage.html')
    elif request.method == "POST":
        file = request.files['file']
        path = 'app/templates/images/garbage/' + file.filename
        file.save(path)

        data = request.values
        create_garbage(data, ds_url=f'images/garbage/{file.filename}')
        return render_template('/forms/form_garbage.html')


@app_views.route('/register/tip/<garbage_id>', methods=['POST'])
def register_comment_view(garbage_id):
    if request.method == "POST":
        data = request.values
        create_comment(data, garbage_id=garbage_id, cooperative_id="", )
        return render_template('/forms/form_garbage.html')

