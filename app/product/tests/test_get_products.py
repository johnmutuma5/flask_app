import json
import unittest
from app.store import store
from app.user.models import User
from . import ProductTestCase

new_product_data = {
	'name': 'product 1',
	'price': 1000
}

new_product_data2 = {
	'name': 'product 2',
	'price': 1500
}

class AddProductTestCase(ProductTestCase):
    def test_users_can_view_all_products_added_by_admin (self):
        admin_login_data = { 'username': 'admin', 'password': 'admin_pass' }
        regular_login_data = { 'username': 'johndoe', 'password': 'test_pass', 'role': 'regular' }
        token = self.helper.authenticate(admin_login_data)
        self.helper.add_product(new_product_data, token)
        self.helper.add_product(new_product_data2, token)
        self.helper.add_user(regular_login_data, token)

        regular_token = self.helper.authenticate(regular_login_data)
        resp = self.helper.get_products(regular_token)
        resp_data = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp_data['ok'])
        self.assertEqual(len(resp_data['products']), 2)
