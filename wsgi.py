# from blog.app import app
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=True)

from blog.app import create_app, db
from werkzeug.security import generate_password_hash

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()

@app.cli.command('create-users')
def create_users():
    from blog.models import User
    db.session.add(
        User(email='a@email.com', password=generate_password_hash('a'))
    )
    db.session.commit()