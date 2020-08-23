from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene.relay import Node, Connection
from app.models import Project, User, Technology


class ProjectObjectType(SQLAlchemyObjectType):
    class Meta:
        model = Project
        interfaces = (Node,)


class ProjectConnection(Connection):
    class Meta:
        node = ProjectObjectType


class UserObjectType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (Node,)


class UserConnection(Connection):
    class Meta:
        node = UserObjectType


class TechnologyObjectType(SQLAlchemyObjectType):
    class Meta:
        model = Technology
        interfaces = (Node,)


class TechnologyConnection(Connection):
    class Meta:
        node = TechnologyObjectType
