from app.models import Project, User, Technology
from app.attributes import ProjectInput, UserInput, TechnologyInput
from app.connections import ProjectObjectType, UserObjectType, TechnologyObjectType
from app.utils import input_to_dict
from sqlalchemy.exc import SQLAlchemyError
import graphene
from sqlalchemy import text


class Query(graphene.ObjectType):

    get_users = graphene.Field(lambda: graphene.List(UserObjectType), input=UserInput())

    def resolve_get_users(self, info, input=None):
        try:
            if not input:
                return User.query.all()

            data = input_to_dict(input=input)

            first_name = data.get("first_name")
            return User.query.filter_by(first_name=first_name).all()

        except SQLAlchemyError as e:
            print(str(e))
            print(info.path)

    get_project = graphene.Field(lambda: graphene.List(ProjectObjectType), input=ProjectInput())

    def resolve_get_project(self, info, input=None):
        try:
            if input:
                data = input_to_dict(input=input)
                query = Project.query
                for key, value in data.items():
                    query = query.filter(text(f"{key}='{value}'"))

                return query.all()

        except SQLAlchemyError as e:
            print(str(e))
            print(info.path)
