from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_required, login_user, logout_user
from riskmanager.decorators import logout_required
from riskmanager.forms import LoginForm

bp = Blueprint('dashboard', __name__)


@bp.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for("dashboard.login"))
    flash("Already logged in")
    return render_template('dashboard.html')


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@bp.route('/login', methods=['POST', 'GET'])
@logout_required
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('signin.html', form=form)
    if form.validate_on_submit():
        login_user(form.user, remember=form.remember.data)
        return redirect(url_for("dashboard.index"))
    flash('Wrong Email/Password combination', 'fail') if form.flash else None
    return render_template('signin.html', form=form)
