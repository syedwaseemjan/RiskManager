# -*- coding: utf-8 -*-
"""
    tests.api.group_tests
    ~~~~~~~~~~~~~~~~~~~~~

    api group tests module
"""

from ..factories import RiskFactory, UserFactory, QuestionFactory, FieldTypeFactory
from . import RiskManagerApiTestCase


class RiskApiTestCase(RiskManagerApiTestCase):

    def _create_fixtures(self):
        super(RiskApiTestCase, self)._create_fixtures()
        self.text_field = FieldTypeFactory()
        self.num_field = FieldTypeFactory()
        self.user = UserFactory()
        self.risk = RiskFactory(insurer=self.user, questions=[
            QuestionFactory(text="Name", type_=self.text_field),
            QuestionFactory(text="Age", type_=self.num_field)])

    def test_get_risks(self):
        r = self.jget('/risks')
        data = self.to_json(r)
        self.assertOkJson(r)
        self.assertEquals(len(data), 1)

    def test_get_risk(self):
        r = self.jget('/risks/1')
        self.assertOkJson(r)
