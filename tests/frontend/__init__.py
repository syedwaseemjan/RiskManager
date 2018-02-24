# -*- coding: utf-8 -*-
"""
    tests.frontend
    ~~~~~~~~~~~~~~

    frontend tests package
"""

from app.frontend import create_app

from .. import RiskManagerAppTestCase, settings


class RiskManagerFrontendTestCase(RiskManagerAppTestCase):

    def _create_app(self):
        return create_app(settings)

    def setUp(self):
        super(RiskManagerFrontendTestCase, self).setUp()
