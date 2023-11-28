
from functools import wraps
from flask import session, flash, render_template, redirect, url_for

def user_role_employeer(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            if session['user_role'] == "employeer":
                return f(*args, **kwargs)
            else:
                flash('You dont have privilege to access this page!', 'danger')
                return render_template("404.html")
        else:
            flash('Unauthorized, Please login!', 'danger')
            return redirect(url_for('login'))
    return wrap


def user_role_user(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            if session['user_role'] == "user":
                return f(*args, **kwargs)
            else:
                flash('You dont have privilege to access this page!', 'danger')
                return render_template("404.html")
        else:
            flash('Unauthorized, Please login!', 'danger')
            return redirect(url_for('login'))
    return wrap

def user_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login!', 'danger')
            return redirect(url_for('login'))
    return wrap