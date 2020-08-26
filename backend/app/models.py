from sqlalchemy import func
from app.constants import db

# Non-static tables

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    handle = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=func.now())
    projects = db.relationship("Project", backref="user")


class Project(db.Model):
    proj_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    name = db.Column(db.String)
    description = db.Column(db.String)
    link = db.Column(db.String)
    technologies = db.relationship(
        "Technology", secondary=lambda: project_technologies, backref="proj_id",
    )


class Technology(db.Model):
    tech_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    purpose = db.Column(db.String)
    project = db.Column(db.Integer, db.ForeignKey("project.proj_id"))


# Static Tables
project_technologies = db.Table(
    'project_technologies',
    db.Column("tech_id", db.Integer, db.ForeignKey("technology.tech_id")),
    db.Column("proj_id", db.Integer, db.ForeignKey("project.proj_id")),
    db.Index("project_technology", "tech_id", "proj_id", unique=True)
)
