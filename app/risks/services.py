from app.extensions import Service
from app.models import Risk


class RiskService(Service):
    __model__ = Risk

    def __init__(self, *args, **kwargs):
        super(RiskService, self).__init__(*args, **kwargs)
