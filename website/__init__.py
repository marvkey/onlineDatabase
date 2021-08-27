from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from userData import User
db = SQLAlchemy()
DB_NAME  = "UserDatabase.db"
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"]="hallo"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .view import views
    app.register_blueprint(views,url_prefix="/")

    from .auth import auth
    app.register_blueprint(auth,url_prefix="/")
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"# trying to acces a page that needs to be login redirect to auth.login()
    login_manager.init_app(app)

    @login_manager.user_loader # stores the id of the user that login so we use id to acces the user
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    if not path.exists("website/"+DB_NAME):
        db.create_all(app=app)
        print("Created Database")