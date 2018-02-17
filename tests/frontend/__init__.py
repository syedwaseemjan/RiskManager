# -*- coding: utf-8 -*-
"""
    tests.frontend
    ~~~~~~~~~~~~~~

    frontend tests package
"""

from riskmanager.frontend import create_app

from .. import AddressBookAppTestCase, settings


class AddressBookFrontendTestCase(AddressBookAppTestCase):

    def _create_app(self):
        return create_app(settings)

    def setUp(self):
        super(AddressBookFrontendTestCase, self).setUp()
        self._login()