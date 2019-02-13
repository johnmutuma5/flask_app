from . import app
from .index import index
from .user.urls import user
from .product.urls import product

app.add_url_rule('/', view_func=index)
app.register_blueprint(user, url_prefix='/users')
app.register_blueprint(product, url_prefix='/products')
