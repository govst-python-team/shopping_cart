from django.test import TestCase

from shop.models import Product


class TestProduct(TestCase):
    fixtures = ['shop']

    def test__str__(self):
        product = Product.objects.get(pk=1)
        self.assertEqual(str(product), product.name)

    def test_get_absolute_url(self):
        product = Product.objects.get(pk=1)
        self.assertEqual(product.get_absolute_url(), '/1/')
