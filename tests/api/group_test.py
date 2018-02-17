# -*- coding: utf-8 -*-
"""
    tests.api.group_tests
    ~~~~~~~~~~~~~~~~~~~~~

    api group tests module
"""

from ..factories import GroupFactory, PersonFactory
from . import AddressBookApiTestCase


class GroupApiTestCase(AddressBookApiTestCase):

    def _create_fixtures(self):
        super(GroupApiTestCase, self)._create_fixtures()
        self.person = PersonFactory()
        self.group = GroupFactory(persons=[self.person])
        self.p = PersonFactory()

    def test_get_groups(self):
        r = self.jget('/groups')
        self.assertOkJson(r)

    def test_get_group(self):
        r = self.jget('/groups/%s' % self.group.id)
        self.assertOkJson(r)

    def test_create_group(self):
        r = self.jpost('/groups', data={
            'name': 'My Group'
        })
        self.assertOkJson(r)
        self.assertIn('"name": "My Group"', r.data)

    def test_create_invalid_group(self):
        r = self.jpost('/groups', data={
            'name': ''
        })
        self.assertBadJson(r)
        self.assertIn('"errors": {', r.data)

    def test_update_group(self):
        r = self.jpost('/groups/%s/update' % self.group.id, data={
            'name': 'My New Group'
        })
        self.assertOkJson(r)
        self.assertIn('"name": "My New Group"', r.data)

    def test_delete_group(self):
        r = self.jget('/groups/%s/delete' % self.group.id)
        self.assertStatusCode(r, 204)

    def test_get_persons(self):
        r = self.jget('/groups/%s/persons' % self.group.id)
        self.assertOkJson(r)

    def test_add_person(self):
        e = '/groups/%s/persons/%s' % (self.group.id, self.p.id)
        r = self.jget(e)
        self.assertOkJson(r)

    def test_remove_person(self):
        e = '/groups/%s/persons/%s/delete' % (self.group.id, self.person.id)
        r = self.jget(e)
        self.assertStatusCode(r, 204)
