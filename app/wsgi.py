from flask import Flask

app = Flask(__name__)

app.config.from_object('config.env')
app.url_map.strict_slashes = False
