# -*- coding: utf-8 -*-

from functools import wraps

from flask import session, request, redirect, url_for



#http://flask.pocoo.org/docs/patterns/viewdecorators/
def login_required(f):
    from model import User
    @wraps(f)
    def decorated_function(*args, **kwargs):
        r = request.path
        if "user" not in session:
            return redirect(url_for('login', r=r))
        return f(*args, **kwargs)
    return decorated_function

