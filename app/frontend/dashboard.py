import os
from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__,
               url_prefix='',
               static_url_path='/dist',
               static_folder='./app/dist',
               template_folder='./app/',
               )


@bp.route('/')
def index():
    return render_template('index.html', env=os.environ.get('env') or 'Kutta')
