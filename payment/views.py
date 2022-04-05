import braintree

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

from orders.models import Order, OrderItem
from .tasks import send_email


# instantiate Braintree payment gateway
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


def payment_process(request, id):

    order = get_object_or_404(Order, id=id, paid=False)
    items = OrderItem.objects.filter(order=order).select_related('product')
    total_sum = sum([x.price * x.quantity for x in items])

    if request.method == 'POST':

        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = gateway.transaction.sale({
            'amount': f'{total_sum}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })

        if result.is_success:
            order.paid = True
            order.transactions_id = result.transaction.id
            send_email.delay(order.email, order.id)  # celery task
            order.save()
            return redirect('done')
        else:
            return redirect('canceled')
    else:
        client_token = gateway.client_token.generate()

        context = {'order': order, 'client_token': client_token}
        return render(request, 'payment/process.html', context)


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
