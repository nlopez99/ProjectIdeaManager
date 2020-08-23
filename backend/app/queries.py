from app.models import Project, User, Technology
from app.attributes import ProjectInput, UserInput, TechnologyInput
from app.connections import ProjectObjectType, UserObjectType, TechnologyObjectType
from app.utils import input_to_dict
from sqlalchemy.exc import SQLAlchemyError
import graphene


class Query(graphene.ObjectType):

    get_users = graphene.Field(lambda: graphene.List(UserObjectType), input=UserInput())

    def resolve_get_users(self, info, input):
        try:
            data = input_to_dict(input=input)

            first_name = data.get("first_name")
            return User.query.filter_by(first_name=first_name).all()

        except SQLAlchemyError as e:
            print(str(e))
            print(info.path)