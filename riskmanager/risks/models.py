from riskmanager.extensions import db
from riskmanager.utils import JsonSerializer


class RiskJsonSerializer(JsonSerializer):
    __json_hidden__ = ['groups']


class Risk(RiskJsonSerializer, db.Model):
    __tablename__ = 'risks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    fields = db.relationship('Field', backref=db.backref('risk'))


class FieldJsonSerializer(JsonSerializer):
    __json_hidden__ = ['persons']


class Field(FieldJsonSerializer, db.Model):
    __tablename__ = 'fields'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, db.ForeignKey('persons.id'))
    field_type = db.relationship('FieldType', backref=db.backref('risk'))

    def __init__(self, email):
        self.email = email


class FieldTypeJsonSerializer(JsonSerializer):
    __json_hidden__ = ['persons']


class FieldType(FieldTypeJsonSerializer, db.Model):
    __tablename__ = 'field_types'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'))
    address = db.Column(db.String(255))

    def __init__(self, address):
        self.address = address
