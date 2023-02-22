from django.test import TestCase
from django.contrib.auth.models import User


class ecommerceTestCase(TestCase):
    def test_auth_cart(self):
        response = self.client.get('/get-cart')
        self.assertRedirects(response, '/login?next=/get-cart')

    def setUp(self):
        self.credentials = {
            'username': 'Test',
            'password': 'long_password'}
        User.objects.create_user(**self.credentials)

    def test_login_true(self):
        logged_in = self.client.login(username='Test', password='long_password')
        self.assertTrue(logged_in)
