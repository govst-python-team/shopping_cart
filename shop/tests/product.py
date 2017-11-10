from django.test import TestCase

from shop.models import Product


class ProductModelTest(TestCase):
    def test_string_representation(self):
        product = Product(name="Snakes on a Plane")
        self.assertEqual(str(product), product.name)



