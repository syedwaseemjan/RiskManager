# -*- coding: utf-8 -*-
"""
    tests.factories
    ~~~~~~~~~~~~~~~

    RiskManager test factories module
"""

import factory
from factory.alchemy import SQLAlchemyModelFactory

from app.extensions import db
from app.models import *


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    class Meta:
        model = User
    name = factory.Sequence(lambda n: 'User Name {0}'.format(n))
    email = factory.Sequence(lambda n: 'user{0}@riskmanager.com'.format(n))


class RiskFactory(BaseFactory):
    class Meta:
        model = Risk
    name = factory.Sequence(lambda n: 'Risk Name {0}'.format(n))
    details = factory.Sequence(lambda n: 'Risk Details {0}'.format(n))


class QuestionFactory(BaseFactory):
    class Meta:
        model = Question
    text = factory.Sequence(lambda n: 'Question Text {0}'.format(n))


class FieldTypeFactory(BaseFactory):
    class Meta:
        model = FieldType
    name = factory.Iterator(["text", "number", "date"])
