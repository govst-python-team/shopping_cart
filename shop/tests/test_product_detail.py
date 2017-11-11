from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from shop.views import product_detail


class TestProductDetail(TestCase):
    fixtures = ['shop']

    def test_product_id_1_resolves_product_detail_template(self):
        found = resolve('/1/')
        self.assertEqual(found.func, product_detail)

    def test_product_id_1_returns_the_correct_html(self):
        request = HttpRequest()
        response = product_detail(request, 1)
        self.assertTrue(response.status_code, 200)
        self.assertIn(b'<h1>Harry Potter and the Chamber of Secrets</h1>', response.content)
