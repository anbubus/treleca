from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='uiui'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .view import views
    from .auth import auths

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auths, url_prefix='/')

    from .models import User, Task
    with app.app_context():
        db.create_all()

    return app

