from app.attributes import ProjectInput, UserInput, TechnologyInput
from app.connections import ProjectObjectType, UserObjectType, TechnologyObjectType
from app.models import Project, User, Technology
from app.utils import save_changes, remove_row, input_to_dict
from app.constants import db
from sqlalchemy.exc import SQLAlchemyError


import graphene
from graphene import Mutation


class CreateUser(Mutation):
    user = graphene.Field(lambda: UserObjectType)

    class Arguments:
        input = UserInput(required=True)
        input.first_name.required = True
        input.last_name.required = True
        input.email.required = True

    def mutate(self, info, input):

        data = input_to_dict(input=input)
        user = User(**data)

        try:
            save_changes(user)

        except SQLAlchemyError as e:
            print(str(e))
            print(info.path)
            db.session.rollback()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()