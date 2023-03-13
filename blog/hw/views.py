from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

hw = Blueprint('hw', __name__, url_prefix='/hw', static_folder='../static')


# # USERS = ['Alise', 'Jon', 'Mike']
# USERS = {
#     1: 'Alice',
#     2: 'Jon',
#     3: 'Mike',
# }


ATICLES = {
    1: {'text': 'asd', 'author': 1},
    2: {'text1': 'asds', 'author': 2},
}
#
#
# @user.route('/')
# def user_list():
#     return render_template('users/list.html', users=USERS, artic=ATICLES, )
#
#
# @user.route('/<int:pk>')
# def get_user(pk: int):
#     try:
#         user_name = USERS[pk]
#     except KeyError:
#         raise NotFound(f'User id {pk} not found')
#     return render_template('users/details.html', user_name=user_name,)
