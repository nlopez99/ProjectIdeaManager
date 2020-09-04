from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from schema import schema
import os


application = Flask(__name__)

application.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "SQLALCHEMY_DATABASE_URI"
)
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
jwt = JWTManager(application)
CORS(application)


def register():
    print("Hello World!")
    return jsonify({"requests": "something"})
     


application.add_url_rule(
    "/", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
)
application.add_url_rule(
    "/users/register", view_func=register 
)