from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

hw = Blueprint('hw', __name__, url_prefix='/hw', static_folder='../static')

AUTHOR = {
    1: 'Pushkin',
    2: 'Lermontov',
    3: 'Lomonosov',
}

ARTICLES = {
    1: {'text': 'Евгений Онегин', 'author': 1},
    2: {'text': 'Герой нашего времени', 'author': 2},
    7: {'text': 'Оды', 'author': 3},
}


@hw.route('/')
def user_list():
    return render_template('hw/list.html', aticles=ARTICLES, authors=AUTHOR, )


@hw.route('/<int:pk>')
def get_user(pk: int):
    print(pk)
    try:
        user_name = AUTHOR[pk]
    except KeyError:
        raise NotFound(f'User id {pk} not found')
    return render_template('hw/details.html', user_name=user_name,)
