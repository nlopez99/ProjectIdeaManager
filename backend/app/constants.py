from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


application = Flask(__name__)

application.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "SQLALCHEMY_DATABASE_URI"
)
db = SQLAlchemy(application)