class RiskManagerError(Exception):
    """Base application error class."""

    def __init__(self, msg):
        self.msg = msg


class RiskDoesNotExist(RiskManagerError):

    def __init__(self):
        super(RiskDoesNotExist, self).__init__(
            "No risk record found for the provided ID. Are you sure you have provided correct ID?")


class RiskManagerFormError(Exception):
    """Raise when an error processing a form occurs."""

    def __init__(self, errors=None):
        self.errors = errors
