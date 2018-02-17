from functools import wraps

from flask import redirect, flash
from flask_login import current_user


def logout_required(fn):
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated:
            flash('You are already logged in.', 'info')
            return redirect('/')
        return fn(*args, **kwargs)
    return decorated_view
