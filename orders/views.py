from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from .models import Order, OrderItem
from store.models import Product
from .forms import OrderForm


def order(request):
    order, created = Order.objects.get_or_create(
        customer=request.user, paid=False)
    items = OrderItem.objects.filter(order=order).select_related('product')

    total_sum = sum([x.price * x.quantity for x in items])
    total_items = sum([x.quantity for x in items])

    context = {'order': order, 'items': items,
               'total_sum': total_sum, 'total_items': total_items}
    return render(request, 'orders/cart.html', context)


def checkout(request):
    order = get_object_or_404(Order, customer=request.user, paid=False)
    order_form = OrderForm(instance=order)

    if request.method == 'POST':
        order_form = OrderForm(request.POST, instance=order)
        if order_form.is_valid():
            order_form.save()
            return redirect('process', order.id)
        else:
            order_form = OrderForm()

    items = OrderItem.objects.filter(order=order).select_related('product')
    total_sum = sum([x.price * x.quantity for x in items])
    total_items = sum([x.quantity for x in items])

    context = {'order': order, 'items': items, 'total_sum': total_sum,
               'total_items': total_items, 'order_form': order_form}
    return render(request, 'orders/checkout.html', context)


def add_to_cart(request, slug):
    product = get_object_or_404(Product, product_slug=slug)
    order, created = Order.objects.get_or_create(
        customer=request.user, paid=False)
    try:
        item = get_object_or_404(OrderItem, order=order, product=product)
        if item:
            messages.add_message(request, messages.INFO,
                                 'Current item is already in the cart!!!')
        else:
            item = OrderItem.objects.create(order=order, product=product,
                                            price=product.product_price)
    except:
        item = OrderItem.objects.create(order=order, product=product,
                                        price=product.product_price)
        messages.add_message(request, messages.SUCCESS, 'Added to the cart!!!')

    return redirect('products', product.product_category.category_slug)


def remove_item(request, id):
    order = get_object_or_404(Order, customer=request.user, paid=False)
    item = get_object_or_404(OrderItem, order=order, id=id)
    item.delete()
    order.save()

    return redirect('cart')
