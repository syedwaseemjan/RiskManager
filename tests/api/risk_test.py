# -*- coding: utf-8 -*-
"""
    tests.api.group_tests
    ~~~~~~~~~~~~~~~~~~~~~

    api group tests module
"""

from ..factories import RiskFactory, UserFactory
from . import RiskManagerApiTestCase


class RiskApiTestCase(RiskManagerApiTestCase):

    def _create_fixtures(self):
        super(RiskApiTestCase, self)._create_fixtures()
        self.user = UserFactory()
        self.risk = RiskFactory(insurer=self.user)

    def test_get_risks(self):
        r = self.jget('/risks')
        print(r)
        print("------------------gggggg---------------")
        self.assertOkJson(r)

    def test_get_risk(self):
        r = self.jget('/risks/%s' % self.risk.id)
        self.assertOkJson(r)
