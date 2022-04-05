from django.core.mail import send_mail

from core.celery import app


@app.task(bind=True)
def send_email(self, user_email, order_id):

    send_mail(
        f'Flower shop: order-{order_id}',
        'Your payment was successfully confirmed.',
        'alexis.nishimura.fake@gmail.com',
        [user_email],
        fail_silently=False,
    )
