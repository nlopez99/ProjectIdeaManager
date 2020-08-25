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


class UpdateUser(Mutation):
    user = graphene.Field(lambda: UserObjectType)

    class Arguments:
        input = UserInput(required=True)
        input.user_id.required = True

    def mutate(self, info, input):
        if input:
            data = input_to_dict(input=input)
            user_id = data.pop("user_id")
            if not user_id:
                raise Exception("No user_id provided for update.")
            try:
                user = User.query.filter_by(user_id=user_id).first()
                [setattr(user, key, value) for key, value in data.items()]

                save_changes(user)

            except SQLAlchemyError as e:
                print(str(e))
                print(info.path)
                db.session.rollback()

        return UpdateUser(user=user)


class DeleteUser(Mutation):
    user = graphene.Field(lambda: UserObjectType)

    class Arguments:
        input = UserInput(required=True)
        input.user_id.required = True

    def mutate(self, info, input):
        if input:
            data = input_to_dict(input=input)
            user_id = data.pop("user_id")

            if not user_id:
                raise Exception("No user_id provided for update.")
            try:
                user = User.query.filter_by(user_id=user_id).first()
                db.session.delete(user)
                db.session.commit()

            except SQLAlchemyError as e:
                print(str(e))
                print(info.path)
                db.session.rollback()

        return DeleteUser(user=user)


class CreateProject(Mutation):
    project = graphene.Field(lambda: ProjectObjectType)

    class Arguments:
        input = ProjectInput(required=True)
        input.name.required = True

    def mutate(self, info, input):

        data = input_to_dict(input=input)
        project = Project(**data)

        try:
            save_changes(project)

        except SQLAlchemyError as e:
            print(str(e))
            print(info.path)
            db.session.rollback()

        return CreateProject(project=project)


class UpdateProject(Mutation):
    project = graphene.Field(lambda: ProjectObjectType)

    class Arguments:
        input = ProjectInput(required=True)
        input.proj_id.required = True

    def mutate(self, info, input):

        if input:
            data = input_to_dict(input=input)
            proj_id = data.pop("proj_id")
            if not proj_id:
                raise Exception("No proj_id provided for update.")
            try:
                project = Project.query.filter_by(proj_id=proj_id).first()
                [setattr(project, key, value) for key, value in data.items()]

                save_changes(project)

            except SQLAlchemyError as e:
                print(str(e))
                print(info.path)
                db.session.rollback()

        return UpdateProject(project=project)


class DeleteProject(Mutation):
    project = graphene.Field(lambda: ProjectObjectType)

    class Arguments:
        input = ProjectInput(required=True)
        input.proj_id.required = True

    def mutate(self, info, input):
        if input:
            data = input_to_dict(input=input)
            proj_id = data.pop("proj_id")

            if not proj_id:
                raise Exception("No proj_id provided for update.")
            try:
                project = Project.query.filter_by(proj_id=proj_id).first()
                db.session.delete(project)
                db.session.commit()

            except SQLAlchemyError as e:
                print(str(e))
                print(info.path)
                db.session.rollback()

        return DeleteProject(project=project)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_project = DeleteProject.Field()
