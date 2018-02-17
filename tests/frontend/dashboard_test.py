# -*- coding: utf-8 -*-
"""
    tests.api.user_tests
    ~~~~~~~~~~~~~~~~~~~~

    api user tests module
"""

from . import RiskManagerFrontendTestCase


class DashboardTestCase(RiskManagerFrontendTestCase):

    def test_authenticated_dashboard_access(self):
        r = self.get('/')
        self.assertOk(r)
        self.assertIn('Risk Manager', r.data)
