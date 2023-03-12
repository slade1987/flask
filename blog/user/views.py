from flask import Blueprint, render_template

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = ['Alise', 'Jon', 'Mike']


@user.route('/')
def user_list():
    return render_template('users/list.html')


@user.route('/<pk>')
def get_user(pk: int):
    return pk
