# -*- coding: utf-8 -*-
"""
    tests.api
    ~~~~~~~~~

    api tests package
"""

from app.api import create_app

from .. import RiskManagerAppTestCase, settings


class RiskManagerApiTestCase(RiskManagerAppTestCase):

    def _create_app(self):
        return create_app(settings, register_security_blueprint=True)

    def setUp(self):
        super(RiskManagerApiTestCase, self).setUp()
