from mongoengine import connect

from sphog_be.config import config
from sphog_be.db.documents import Photo, PhotoUrls, Topic
from sphog_be.unsplash import Unsplash


def hydrate_photos(unsplash: Unsplash, topic: Topic):
    per_page = 30
    api_photos = unsplash.topics.get_photos(
        topic["id"], order_by="oldest", page=1, per_page=per_page
    )

    for api_photo in api_photos["response"]["results"]:
        photo = Photo(
            id=api_photo["id"],
            description=api_photo["description"],
            topics=[topic],
            urls=PhotoUrls(**api_photo["urls"]),
        )
        photo.save()


def hydrate_topics(unsplash: Unsplash):
    per_page = 30
    api_topics = unsplash.topics.list(page=1, per_page=per_page)

    for api_topic in api_topics["response"]["results"]:
        topic = Topic(id=api_topic["id"], title=api_topic["title"])
        topic.save()


def hydrate_db():
    unsplash = Unsplash(config.get("UNSPLASH_ACCESS_KEY"))
    hydrate_topics(unsplash)

    for topic in Topic.objects():
        hydrate_photos(unsplash, topic)


if __name__ == "__main__":
    connect(config["MONGODB_SETTINGS"]["db"])
    hydrate_db()
