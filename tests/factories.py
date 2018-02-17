# -*- coding: utf-8 -*-
"""
    tests.factories
    ~~~~~~~~~~~~~~~

    OnlineAddressBook test factories module
"""


from factory import Sequence, LazyAttribute
from factory.alchemy import SQLAlchemyModelFactory
from passlib.hash import bcrypt

from riskmanager.extensions import db
from riskmanager.models import *


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = db.session


class AdminFactory(BaseFactory):
    class Meta:
        model = Admin
    email = Sequence(lambda n: 'user{0}@riskmanager.com'.format(n))
    _password = LazyAttribute(lambda a: bcrypt.encrypt('password'))
    active = True


class PersonFactory(BaseFactory):
    class Meta:
        model = Person
    first_name = Sequence(lambda n: 'Person First Name {0}'.format(n))
    last_name = Sequence(lambda n: 'Person Last Name {0}'.format(n))


class AddressFactory(BaseFactory):
    class Meta:
        model = Address
    address = Sequence(lambda n: 'Address {0}'.format(n))


class EmailFactory(BaseFactory):
    class Meta:
        model = Email
    email = Sequence(lambda n: 'user{0}@riskmanager.com'.format(n))


class PhoneFactory(BaseFactory):
    class Meta:
        model = Phone
    phone = Sequence(lambda n: 'Phone Number {0}'.format(n))


class GroupFactory(BaseFactory):
    class Meta:
        model = Group
    name = Sequence(lambda n: 'Group Number {0}'.format(n))
