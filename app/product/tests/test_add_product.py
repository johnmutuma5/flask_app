import json
import unittest
from app.store import store
from app.user.models import User
from . import ProductTestCase

new_product_data = {
	'name': 'product 2',
	'price': 1500
}

class AddProductTestCase(ProductTestCase):
    def test_it_adds_a_product (self):
        login_data = { 'username': 'admin', 'password': 'admin_pass' }
        token = self.helper.authenticate(login_data)
        resp = self.helper.add_product(new_product_data, token)
        resp_data = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp_data['ok'])
        self.assertEqual(resp_data['product']['name'], new_product_data['name'])

    def test_non_admin_users_do_not_add_products(self):
        user_data = { 'username': 'john_doe4', 'password': 'test_pass', 'role': 'regular'}
        store.add_user(User(user_data))
        token = self.helper.authenticate(user_data)
        resp = self.helper.add_product(new_product_data, token)
        resp_data = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 403)
        self.assertFalse(resp_data['ok'])
        self.assertEqual(resp_data['message'], 'Please provide admin credentials')
