from django.core.urlresolvers import resolve
from django.test import TestCase

from shop.views import product_list


class TestProductList(TestCase):
    fixtures = ['shop']

    def test_index_returns_product_list(self):
        found = resolve('/')
        self.assertEqual(found.func, product_list)
