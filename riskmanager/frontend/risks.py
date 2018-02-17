from flask import Blueprint, render_template
from riskmanager.forms import NewPersonForm

bp = Blueprint('persons', __name__)


@bp.route('/new-person', methods=['GET', 'POST'])
def new():
    form = NewPersonForm()
    if form.validate_on_submit():
        return render_template('persons/new_person.html', form=form)
    return render_template('persons/new_person.html', form=form)


@bp.route('/persons/<int:person_id>')
def show(person_id):
    return render_template('persons/show.html')
