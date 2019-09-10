
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .database_handler import CustomBaseQuery


app = Flask(__name__)
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app, CustomBaseQuery)

migrate = Migrate(app, db)

from luizalabs_flask import routes
