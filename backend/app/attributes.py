from graphene import InputObjectType, String, Int, List, DateTime


class ProjectInput(InputObjectType):
    proj_id = Int()
    user_id = Int()
    name = String()
    description = String()
    link = String()
    technologies = List(String)


class UserInput(InputObjectType):
    id = Int()
    first_name = String()
    last_name = String()
    handle = String()
    email = String()
    password = String()
    created_at = DateTime()
    projects = List(Int)


class TechnologyInput(InputObjectType):
    tech_id = Int()
    name = String()
    purpose = String()
