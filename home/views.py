from products.models import Product
from django.shortcuts import render

# Create your views here.


def index(request):
    """A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)

def products(request):
    """A view to show all products, including sorting and search queries """

    product = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html')