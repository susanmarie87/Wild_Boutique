""" Views"""
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the cart items"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add multiple products to shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def update_bag(request, item_id):
    """A view to update the bag items"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to (bag[item_id])')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} quantity to (bag[item_id])')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def delete_bag_item(request, item_id):
    """A view to delete bag items"""

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    bag.pop(item_id)

    request.session['bag'] = bag
    messages.success(request, f'Removed {product.name} quantity to (bag[item_id])')

    return redirect(reverse('view_bag'))
