from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object('config.env')

from app import urls
