from flask_script import Manager

from riskmanager.api import create_app
from riskmanager.extensions import db
from riskmanager.models import Admin

manager = Manager(create_app())


@manager.command
def test():
    pass


@manager.command
def create_db():
    db.create_all()


@manager.command
def init_db():
    create_admin()


@manager.command
def create_admin():
    admin = Admin()
    admin.email = "admin@riskmanager.com"
    admin.password = "test123"
    admin.active = True
    db.session.add(admin)

    db.session.commit()


if __name__ == "__main__":
    manager.run()
