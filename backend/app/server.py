from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from flask_cors import CORS
from app.schema import schema
import os


def create_app():
    application = Flask(__name__)

    application.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI"
    )
    application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db = SQLAlchemy(application)
    CORS(application)
    application.add_url_rule(
        "/", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
    )

    return application
