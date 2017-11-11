from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from shop.views import product_list


class TestProductList(TestCase):
    fixtures = ['shop']

    def test_index_returns_product_list(self):
        found = resolve('/')
        self.assertEqual(found.func, product_list)

    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = product_list(request)
        self.assertTrue(response.status_code, 200)
        self.assertIn(b'/1/">Harry Potter and the Chamber of Secrets</a>', response.content)
