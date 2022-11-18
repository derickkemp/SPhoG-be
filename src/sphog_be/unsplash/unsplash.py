# NotRequired will only be included in Python 3.11, we polyfill it if the import fails
try:
    from typing import NotRequired
except ImportError:
    from typing_extensions import NotRequired

from typing import Literal, TypedDict

from requests import get


class UnsplashResult(TypedDict):
    errors: NotRequired[list]
    response: NotRequired[dict]


class Unsplash:
    def __init__(self, access_key: str) -> None:
        self.access_key = access_key
        self.topics = Topics(self)


class Topics:
    def __init__(self, unsplash: Unsplash) -> None:
        self.unsplash = unsplash

    def get_photos(
        self,
        topic_id_or_slug: str,
        order_by: Literal["latest, oldest, popular"] = "latest",
        page: int = 1,
        per_page: int = 30,
    ) -> UnsplashResult:
        resp = get(
            f"https://api.unsplash.com/topics/{topic_id_or_slug}/photos",
            headers={"Authorization": f"Client-ID {self.unsplash.access_key}"},
            params={"order_by": order_by, "page": page, "per_page": per_page},
        )

        total = resp.headers["x-total"]

        return {"response": {"results": resp.json(), "total": total}}

    def list(self, page: int = 1, per_page=30) -> UnsplashResult:
        resp = get(
            "https://api.unsplash.com/topics",
            headers={"Authorization": f"Client-ID {self.unsplash.access_key}"},
            params={"page": page, "per_page": per_page},
        )

        total = resp.headers["x-total"]

        return {"response": {"results": resp.json(), "total": total}}
