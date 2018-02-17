from flask_wtf import Form
from wtforms import Form as WTForm, TextField, PasswordField, \
    BooleanField, FieldList, HiddenField, FormField
from wtforms.validators import Required, Length, Optional
from riskmanager.models import Admin, Group
from wtforms.ext.sqlalchemy.fields import QuerySelectField

__all__ = ['LoginForm', 'NewPersonForm', 'UpdatePersonForm']


def get_groups():
    return Group.query.all()


class LoginForm(Form):
    email = TextField(u'',
                      validators=[Required(u'Email is mandatory.')])
    password = PasswordField(u'',
                             validators=[Required(u'Password is mandatory.'),
                                         Length(min=6,
                                                message=u'Password length '
                                                        u'must be >5.')])
    remember = BooleanField(u'Remember Me')

    def validate(self):
        self.flash = False
        rv = Form.validate(self)
        if not rv:
            return False

        query = Admin.query.filter(Admin.email.ilike(self.email.data))
        user = query.first()
        if user is None:
            self.flash = True
            return False

        if not user.match_password(self.password.data):
            self.flash = True
            return False

        self.user = user
        return True


class AddressForm(WTForm):
    address_id = HiddenField()
    name = TextField()


class EmailForm(WTForm):
    email_id = HiddenField()
    name = TextField()


class PhoneForm(WTForm):
    phone_id = HiddenField()
    name = TextField()


class GroupForm(WTForm):
    group_id = HiddenField()
    name = QuerySelectField(query_factory=get_groups, blank_text='')


class NewPersonForm(Form):
    first_name = TextField('First Name', validators=[Required()])
    last_name = TextField('Last Name', validators=[Required()])

    addresses = FieldList(FormField(AddressForm), min_entries=1)
    emails = FieldList(FormField(EmailForm), min_entries=1)
    phones = FieldList(FormField(PhoneForm), min_entries=1)
    groups = FieldList(FormField(GroupForm), min_entries=1)


class UpdatePersonForm(Form):
    name = TextField('Name', validators=[Optional()])
    address = TextField('Address', validators=[Optional()])
    city = TextField('City', validators=[Optional()])
    state = TextField('State', validators=[Optional()])
    zip_code = TextField('Zip Code', validators=[Optional()])
