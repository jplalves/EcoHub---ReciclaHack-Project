from app.actions.users_actions import login
from flask import Blueprint, render_template, request, redirect


app_views = Blueprint('views', __name__)


# Templates
@app_views.route('/', methods=['GET'])
def home_view():
    # _json = request.get_json()
    return render_template('index.html')


@app_views.route('/how_to_recycle', methods=['GET'])
def how_to_recycle_view():
    # _json = request.get_json()
    return render_template('index.html')


@app_views.route('/where_recycle', methods=['GET'])
def where_recycle_view():
    # _json = request.get_json()
    return render_template('index.html')


@app_views.route('/login_or_register', methods=['POST', 'GET'])
def login_view():
    if request.method == 'GET':
        return render_template('login.html', status=True)

    credentials = request.values
    if login(credentials.get('email'), credentials.get("password")):
        return redirect('/')
    return render_template('login.html', status=False)

