# -*- coding: utf-8 -*-
"""
    tests.api
    ~~~~~~~~~

    api tests package
"""

from riskmanager.api import create_app

from .. import AddressBookAppTestCase, settings


class AddressBookApiTestCase(AddressBookAppTestCase):

    def _create_app(self):
        return create_app(settings, register_security_blueprint=True)

    def setUp(self):
        super(AddressBookApiTestCase, self).setUp()
        self._login()
