import json
import unittest
from app import app
from ..user.models import User
from ..store import store

class BaseAPITestSetUp (unittest.TestCase):
    def setUp(self):
        self.helper = TestHelper(app.test_client())
        store.init_db()
        default_admin = {
            'username': 'admin',
            'password': 'admin_pass',
            'role': 'admin'
        }
        user = User(default_admin)
        store.add_user(user)

    def tearDown(self):
        store.drop_db()



class TestHelper():
    def __init__(self, test_client):
        self.base_url = 'http://127.0.0.1:8080'
        self.headers = {'content-type': 'application/json'}
        self.client = test_client

    def authenticate (self, login_data):
        url = f'{self.base_url}/users/auth'
        res = self.client.post(url, data=json.dumps(login_data), headers=self.headers)
        # return the token
        return json.loads(res.data.decode('utf8'))['token']

    def add_user (self, user_data, token):
        url = f'{self.base_url}/users'
        return self.client.post(
            url,
            data=json.dumps(user_data),
            headers={ **self.headers, 'token': token }
        )

    def add_product (self, product_data, token):
        url = f'{self.base_url}/products'
        return self.client.post(
            url,
            data=json.dumps(product_data),
            headers={ **self.headers, 'token': token }
        )

    def get_products (self, token):
        url = f'{self.base_url}/products'
        return self.client.get(url, headers={ **self.headers, 'token': token })
