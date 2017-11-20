from unittest import TestCase

from django.test import RequestFactory

from cart.cart import Cart


class TestCart(TestCase):
    fixtures = ['shop.yaml']

    def setUp(self):
        self.request = RequestFactory()
        self.request.session = {}

    def test___init__(self):
        cart = Cart(self.request)
        self.assertEqual(cart.session, self.request.session)
