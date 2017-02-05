from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/mydatabase.db'
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
