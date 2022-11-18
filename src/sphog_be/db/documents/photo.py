from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ListField,
    ReferenceField,
    StringField,
)

from .topic import Topic


class PhotoUrls(EmbeddedDocument):
    full = StringField()
    raw = StringField()
    regular = StringField()
    small = StringField()
    small_s3 = StringField()
    thumb = StringField()


class Photo(Document):
    id = StringField(primary_key=True)
    description = StringField()
    topics = ListField(ReferenceField(Topic))
    urls = EmbeddedDocumentField(PhotoUrls)
