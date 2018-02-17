# -*- coding: utf-8 -*-
"""
    tests
    ~~~~~

    tests package
"""

from unittest import TestCase

from riskmanager.extensions import db

from .utils import FlaskTestCaseMixin


class ManagerTestCase(TestCase):
    pass


class RiskManagerAppTestCase(FlaskTestCaseMixin, ManagerTestCase):

    def _create_app(self):
        raise NotImplementedError

    def _create_fixtures(self):
        pass

    def setUp(self):
        super(RiskManagerAppTestCase, self).setUp()
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self._create_fixtures()
        self._create_csrf_token()

    def tearDown(self):
        super(RiskManagerAppTestCase, self).tearDown()
        db.drop_all()
        self.app_context.pop()
