from mongoengine import Document
from mongoengine.fields import StringField, ListField, ReferenceField
from mongoengine import CASCADE

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField(required=True)
