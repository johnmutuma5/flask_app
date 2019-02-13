import json
import unittest
from app.store import store
from app.user.models import User
from . import UserTestCase

new_user_data = {
	'username': 'john_doe4',
	'password': 'test_pass',
	'role': 'regular'
}

class AddUserTestCase(UserTestCase):
    def test_it_adds_a_user(self):
        login_data = { 'username': 'admin', 'password': 'admin_pass' }
        token = self.helper.authenticate(login_data)
        resp = self.helper.add_user(new_user_data, token)
        resp_data = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp_data['ok'])
        self.assertEqual(resp_data['user']['username'], new_user_data['username'])

    def test_it_prevents_regular_user_from_adding_other_users(self):
        user_data = { 'username': 'john_doe4', 'password': 'test_pass', 'role': 'regular'}
        store.add_user(User(user_data))
        token = self.helper.authenticate(user_data)
        resp = self.helper.add_user(new_user_data, token)
        resp_data = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 403)
        self.assertFalse(resp_data['ok'])
        self.assertEqual(resp_data['message'], 'Please provide admin credentials')
