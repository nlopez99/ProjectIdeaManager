from wsgi import db


class Project(db.Model):
    proj_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    technology = db.relationship("technology")


class Technology(db.Model):
