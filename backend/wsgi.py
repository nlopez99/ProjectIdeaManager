from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)


# Features
# Create a Project with Title, Description, Link, To Do Steps, Technology


# TO DO:
# TODO: Define DB Architecture
# TODO: Build SA models
# TODO: Create REST API
# TODO: Build Login and Auth
# TODO: Start Home Page View
