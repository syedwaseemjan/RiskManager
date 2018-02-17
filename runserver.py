# -*- coding: utf-8 -*-
"""
    runserver
    ~~~~

    riskmanager wsgi module
"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from riskmanager import api, frontend

application = DispatcherMiddleware(frontend.create_app(), {
    '/api/v1': api.create_app()
})

if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, application,
               use_reloader=True, use_debugger=True)
