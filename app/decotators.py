from functools import wraps
from flask import abort, flash, redirect, url_for
from flask_login import current_user

def user_has_role(*role_names):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash("You need to be logged in to access this page.")
                return redirect(url_for('auth.login'))
            if not any(current_user.has_role(role) for role in role_names):
                flash("You do not have permission to access this page.")
                return abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
