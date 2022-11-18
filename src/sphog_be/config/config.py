from os import environ
from dotenv import load_dotenv

load_dotenv("../.env.secret"),  # load sensitive variables

config = {
    "MONGODB_SETTINGS": {
        **({"db": environ.get("MONGODB_DB")} or {}),
    },
    "SCHEDULER_API_ENABLED": True,
    **({"UNSPLASH_ACCESS_KEY": environ.get("UNSPLASH_ACCESS_KEY")} or {}),
}
