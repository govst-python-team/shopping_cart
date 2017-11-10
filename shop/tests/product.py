from django.core.management import call_command
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from shop.models import Product
from shop.views import product_detail


class ProductModelTest(TestCase):
    def test_string_representation(self):
        product = Product(name="Snakes on a Plane")
        self.assertEqual(str(product), product.name)


class ProductDetailView(TestCase):
    fixtures = ['shop']

    def test_product_id_1_resolves_to_harry_potter(self):
        found = resolve('/1/')
        self.assertEqual(found.func, product_detail)

    def test_product_id_1_returns_the_correct_html(self):
        request = HttpRequest()
        response = product_detail(request, 1)
        self.assertIn(b'<title>Products</title>', response.content)
        self.assertIn(b'<h1>Harry Potter and the Chamber of Secrets</h1>', response.content)
