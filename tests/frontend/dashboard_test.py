# -*- coding: utf-8 -*-
"""
    tests.api.user_tests
    ~~~~~~~~~~~~~~~~~~~~

    api user tests module
"""

from . import AddressBookFrontendTestCase


class DashboardTestCase(AddressBookFrontendTestCase):
    
    def test_authenticated_dashboard_access(self):
        r = self.get('/')
        self.assertOk(r)
        self.assertIn('section search', r.data)

    def test_unauthenticated_dashboard_access(self):
        self.get('/logout')
        r = self.get('/')
        self.assertOk(r)
        self.assertNotIn('section search', r.data)    