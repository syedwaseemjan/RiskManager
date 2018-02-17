from riskmanager.extensions import db
from riskmanager.utils import JsonSerializer, TimeStampMixin


class UserJsonSerializer(JsonSerializer):
    pass


class User(UserJsonSerializer, db.Model, TimeStampMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(255), unique=True)

    def __str__(self):
        return u'{0}-{1}-{2}'.format(self.id, self.name, self.email)


class RiskJsonSerializer(JsonSerializer):
    __json_hidden__ = ['insurer_id']


class Risk(RiskJsonSerializer, db.Model, TimeStampMixin):
    __tablename__ = 'risks'

    id = db.Column(db.Integer, primary_key=True)
    insurer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    details = db.Column(db.Text)

    insurer = db.relationship('User')

    def __str__(self):
        return u'{0}-{1}-{2}-{3}'.format(self.id, self.insurer_id, self.name, self.details)


class QuestionJsonSerializer(JsonSerializer):

    def to_json(self):
        self.__json_hidden__ = ['risk', 'mcq']
        if self.type_id != 4:
            self.__json_hidden__.append('options')
        if not self.type_id:
            self.__json_hidden__.extend(['risk_id', 'type_id', 'type_'])
        if not self.parent_id:
            self.__json_hidden__.append('parent_id')
        else:
            self.__json_hidden__.extend(['created_on', 'updated_on'])
        return super(QuestionJsonSerializer, self).to_json()


class Question(QuestionJsonSerializer, db.Model, TimeStampMixin):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)

    # risk_id and type_id could be null in case the question is a subfield of enum
    risk_id = db.Column(db.Integer, db.ForeignKey('risks.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('field_types.id'))

    '''
    Text of the question could be anything like 'What is your first name?'
    or simply 'First name'. Other examples are age, zip code, model, serial number
    '''
    text = db.Column(db.String)

    #is_required = db.Column(db.Bool)
    # if a field is a subfield of enum then it will have parent id too.
    # Field with type Enum could only be a parent of other fields.
    parent_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    type_ = db.relationship('FieldType')
    options = db.relationship('Question', remote_side=[parent_id], backref=db.backref('mcq', remote_side=[id]))
    risk = db.relationship('Risk', backref=db.backref('questions'))

    def __str__(self):
        return u'{0}-{1}-{2}-{3}-{4}'.format(self.id, self.risk_id, self.type_id, self.text, self.text, self.parent_id)


"""
class Validation(FieldJsonSerializer, db.Model):
    __tablename__ = 'validations'

    id = db.Column(db.Integer, primary_key=True)
    field_id = db.Column(db.Integer, db.ForeignKey('fields.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('field_types.id'))

    name = db.Column(db.Integer)
    is_required = db.Column(db.Bool)

    type_ = db.relationship('FieldType', backref=db.backref('risk'))
"""


class FieldTypeJsonSerializer(JsonSerializer):
    __json_hidden__ = ['created_on', 'updated_on']


class FieldType(FieldTypeJsonSerializer, db.Model, TimeStampMixin):
    __tablename__ = 'field_types'

    id = db.Column(db.Integer, primary_key=True)
    # text, number, date, or enum
    name = db.Column(db.String(50))

    def __str__(self):
        return u'{0}-{1}'.format(self.id, self.name)


class ApplicationJsonSerializer(JsonSerializer):
    pass


class Application(ApplicationJsonSerializer, db.Model, TimeStampMixin):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    risk_id = db.Column(db.Integer, db.ForeignKey('risks.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    risk = db.relationship('Risk', backref=db.backref('applications'))
    anwsers = db.relationship('Answer', backref=db.backref('application'))

    def __str__(self):
        return u'{0}-{1}-{2}'.format(self.id, self.risk_id, self.user_id)


class AnswerJsonSerializer(JsonSerializer):
    pass


class Answer(AnswerJsonSerializer, db.Model, TimeStampMixin):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey('applications.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    value = db.Column(db.String(250))

    def __str__(self):
        return u'{0}-{1}-{2}-{3}'.format(self.id, self.application_id, self.question_id, self.value)
