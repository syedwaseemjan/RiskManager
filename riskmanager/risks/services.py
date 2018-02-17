from riskmanager.extensions import Service
from riskmanager.models import Risk


class RiskService(Service):
    __model__ = Risk

    def __init__(self, *args, **kwargs):
        super(RiskService, self).__init__(*args, **kwargs)
