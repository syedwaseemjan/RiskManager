# -*- coding: utf-8 -*-
"""
    tests.api.person_tests
    ~~~~~~~~~~~~~~~~~~~~~~~

    api person tests module
"""

from ..factories import AddressFactory, EmailFactory,\
    PhoneFactory, GroupFactory, PersonFactory
from . import AddressBookApiTestCase


class PersonApiTestCase(AddressBookApiTestCase):

    def _create_fixtures(self):
        super(PersonApiTestCase, self)._create_fixtures()
        self.address = AddressFactory()
        self.email = EmailFactory()
        self.phone = PhoneFactory()
        self.group = GroupFactory()
        self.person = PersonFactory(addresses=[self.address],
                                    emails=[self.email],
                                    phones=[self.phone], groups=[self.group])

    def test_get_persons(self):
        r = self.jget('/persons')
        self.assertOkJson(r)

    def test_get_person(self):
        r = self.jget('/persons/%s' % self.person.id)
        self.assertOkJson(r)

    def test_create_persons(self):
        r = self.jpost('/persons', data={
            'first_name': 'New Person First Name',
            'last_name': 'New Person Last Name',
            'addresses-0-name': 'Address New',
            'emails-0-name': 'user_new@riskmanager.com',
            'phones-0-name': 'Phone Number New',
            'groups-0-name': str(self.group.id)
        })
        self.assertOkJson(r)

    def test_create_invalid_person(self):
        r = self.jpost('/persons', data={
            'first_name': 'New Person'
        })
        self.assertBadJson(r)

    def test_update_person(self):
        r = self.jpost('/persons/%s/update' % self.person.id, data={
            'name': 'New Person'
        })
        self.assertOkJson(r)

    def test_delete_person(self):
        r = self.jget('/persons/%s/delete' % self.person.id)
        self.assertStatusCode(r, 204)
