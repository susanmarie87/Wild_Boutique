from django.shortcuts import render


def view_bag(request):
    """ A view that renders the cart items"""

    return render(request, 'bag/bag.html')
