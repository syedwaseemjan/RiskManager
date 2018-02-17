from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__)


@bp.route('/')
def index():
    return render_template('dashboard.html')
