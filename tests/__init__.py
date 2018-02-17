# -*- coding: utf-8 -*-
"""
    tests
    ~~~~~

    tests package
"""

from unittest import TestCase

from riskmanager.extensions import db

from .factories import AdminFactory
from .utils import FlaskTestCaseMixin


class BookTestCase(TestCase):
    pass


class AddressBookAppTestCase(FlaskTestCaseMixin, BookTestCase):

    def _create_app(self):
        raise NotImplementedError

    def _create_fixtures(self):
        self.user = AdminFactory()

    def setUp(self):
        super(AddressBookAppTestCase, self).setUp()
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self._create_fixtures()
        self._create_csrf_token()

    def tearDown(self):
        super(AddressBookAppTestCase, self).tearDown()
        db.drop_all()
        self.app_context.pop()

    def _login(self, email=None, password=None):
        email = email or self.user.email
        password = password or 'password'
        return self.post('/login', data={'email': email, 'password': password},
                         follow_redirects=False)
