from riskmanager.extensions import Service
from riskmanager.models import Risk, Address, Email,\
    Phone


class RiskService(Service):
    __model__ = Risk

    def __init__(self, *args, **kwargs):
        super(RiskService, self).__init__(*args, **kwargs)

    def create_person(self, form):
        person = Risk()
        person.first_name = form.first_name.data
        person.last_name = form.last_name.data
        for aform in form.addresses:
            if aform.data["name"]:
                person.addresses.append(Address(aform.data["name"]))
        for eform in form.emails:
            if eform.data["name"]:
                person.emails.append(Email(eform.data["name"]))
        for pform in form.phones:
            if pform.data["name"]:
                person.phones.append(Phone(pform.data["name"]))
        for gform in form.groups:
            if gform.data["name"]:
                person.groups.append(gform.data["name"])

        self.save(person)
        return person

    def search(self, text):
        print text
        return Risk.query.filter(
            Risk.first_name.ilike(text.strip())).first()

    def _serialize(self, data):
        return {
            "id": data.id,
            "first_name": data.first_name,
            "last_name": data.last_name,
            "addresses": [{"address": x.address} for x in data.addresses],
            "emails": [{"email": x.email} for x in data.emails],
            "phones": [{"phone": x.phone} for x in data.phones],
            "groups": [{"name": x.name, "id": x.id} for x in data.groups]
        }
