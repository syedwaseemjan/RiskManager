from flask import Blueprint
from riskmanager.api import route
from riskmanager.services import risks
from riskmanager.exceptions import RiskDoesNotExist

bp = Blueprint('risks', __name__, url_prefix='/risks')


@route(bp, '/', methods=['GET'])
def list():
    """Returns a list of risk instances."""
    return risks.all()


@route(bp, '/<risk_id>', methods=['GET'])
def show(risk_id):
    """Returns a risk instance."""
    try:
        risk = risks.get_or_404(risk_id)
    except Exception:
        raise RiskDoesNotExist
    return risk
