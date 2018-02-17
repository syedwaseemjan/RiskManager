from flask_script import Manager

from riskmanager.api import create_app
from riskmanager.extensions import db
from riskmanager.models import User, Risk, Question, FieldType

manager = Manager(create_app())


@manager.command
def test():
    pass


@manager.command
def create_db():
    db.create_all()


@manager.command
def init_db():
    text_field = FieldType(name='text')
    db.session.add(text_field)
    num_field = FieldType(name='number')
    db.session.add(num_field)
    date_field = FieldType(name='date')
    db.session.add(date_field)
    enum_field = FieldType(name='enum')
    db.session.add(enum_field)

    user = User()
    user.email = "user1@riskmanager.com"
    user.name = "test1"
    db.session.add(user)
    db.session.commit()

    user = User()
    user.email = "user2@riskmanager.com"
    user.name = "test2"
    db.session.add(user)
    db.session.commit()

    risk = Risk()
    risk.insurer_id = 1
    risk.name = 'Automobile Policies'
    risk.details = 'Automobile Policies Details'

    risk.questions.append(Question(type_id=text_field.id, text='First Name'))
    risk.questions.append(Question(type_id=num_field.id, text='Age'))
    risk.questions.append(Question(type_id=num_field.id, text='Zip code'))
    db.session.add(risk)
    db.session.commit()

    risk = Risk()
    risk.insurer_id = 1
    risk.name = 'Cyber Liability Coverage'
    risk.details = 'Cyber Liability Coverage Details'

    risk.questions.append(Question(type_id=text_field.id, text='Fullname'))
    risk.questions.append(Question(type_id=num_field.id, text='What is your Age?'))
    question = Question(type_id=enum_field.id, text='Number of employees')
    question.options.append(Question(text='Less than 10'))
    question.options.append(Question(text='10 - 20'))
    question.options.append(Question(text='Greater than 20'))
    risk.questions.append(question)
    db.session.add(risk)
    db.session.commit()

    risk = Risk()
    risk.insurer_id = 1
    risk.name = 'Prize Insurance'
    risk.details = '''If someone gets a $1 million hole-in-one prize at a golf tournament,
    the golf course does not pay it, they have an insurance policy to cover them.'''

    risk.questions.append(Question(type_id=text_field.id, text='Name'))
    risk.questions.append(Question(type_id=text_field.id, text='Serial Number'))
    question = Question(type_id=enum_field.id, text='Gender')
    question.options.append(Question(text='Male'))
    question.options.append(Question(text='Female'))
    risk.questions.append(question)
    db.session.add(risk)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
