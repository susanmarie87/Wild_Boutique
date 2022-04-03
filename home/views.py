"""views to render index page and product list"""
from django.shortcuts import render
from products.models import Product


# Create your views here.


def index(request):
    """A view to show all products, including sorting and search queries """

    products_list = Product.objects.all()

    context = {
        'products': products_list,
    }

    return render(request, 'home/index.html', context)

def products(request):
    """A view to show all products, including sorting and search queries """

    products_list = Product.objects.all()

    context = {
        'products': products_list,
    }

    return render(request, 'products/products.html', context)
