from django.shortcuts import render, get_object_or_404
from shop.models import Product


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product/detail.html', {'product': product})
