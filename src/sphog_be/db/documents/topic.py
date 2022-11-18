from mongoengine import Document, StringField


class Topic(Document):
    id = StringField(primary_key=True)
    title = StringField()
