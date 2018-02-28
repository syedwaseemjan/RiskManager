# -*- coding: utf-8 -*-
"""
    tests.frontend.dashboard_tests
    ~~~~~~~~~~~~~~~~~~~~

    frontend dashboard tests module
"""

from . import RiskManagerFrontendTestCase


class DashboardTestCase(RiskManagerFrontendTestCase):

    def test_dashboard_access(self):
        r = self.get('/')
        self.assertOk(r)
        self.assertIn('Risk Manager', r.data)
