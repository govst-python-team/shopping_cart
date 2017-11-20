from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from shop.models import Product


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
