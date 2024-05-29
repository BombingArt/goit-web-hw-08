from mongoengine import Document, StringField, EmailField, BooleanField
import connect


class Contact(Document):
    full_name = StringField(required=True)
    email = EmailField(required=True)
    is_sent = BooleanField(default=False)
