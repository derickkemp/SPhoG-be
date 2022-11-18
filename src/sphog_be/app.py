from flask import Flask

from .config import config
from .scheduler.scheduler import scheduler

# create app
app = Flask(__name__)
app.config.update(**config)

# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()


if __name__ == "__main__":
    app.run()
