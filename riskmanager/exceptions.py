class RiskManagerError(Exception):
    """Base application error class."""

    def __init__(self, msg):
        self.msg = msg


class RiskManagerFormError(Exception):
    """Raise when an error processing a form occurs."""

    def __init__(self, errors=None):
        self.errors = errors
