from app.constants import db


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def remove_row(obj):
    db.session.remove(obj)
    db.session.commit()


def input_to_dict(input):
    dic = {}
    for key in input:
        if input[key] is not None:
            dic[key] = input[key]

    return dic
