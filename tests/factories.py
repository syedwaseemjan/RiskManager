# -*- coding: utf-8 -*-
"""
    tests.factories
    ~~~~~~~~~~~~~~~

    OnlineAddressBook test factories module
"""


from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from riskmanager.extensions import db
from riskmanager.models import *


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    class Meta:
        model = User
    name = Sequence(lambda n: 'Person Name {0}'.format(n))
    email = Sequence(lambda n: 'user{0}@riskmanager.com'.format(n))


class RiskFactory(BaseFactory):
    class Meta:
        model = Risk
    name = Sequence(lambda n: 'Risk Name {0}'.format(n))
    details = Sequence(lambda n: 'Risk Details {0}'.format(n))


class QuestionFactory(BaseFactory):
    class Meta:
        model = Question
    text = Sequence(lambda n: 'Question Text {0}'.format(n))


class FieldTypeFactory(BaseFactory):
    class Meta:
        model = FieldType
    name = Sequence(lambda n: 'Field Type Name {0}'.format(n))
