from _md5 import md5

from flask import session

from models import User


def login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        session['user_id'] = user.id
        return True
    return False


def logout():
    session.pop('user_id', 0)


def get_user():
    user_id = session.get('user_id')
    if not user_id:
        return None
    user = User.query.filter_by(id=user_id).first()
    return user


def is_authorized():
    return bool(session.get('user_id'))
