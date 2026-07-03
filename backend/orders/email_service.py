from django.core.mail import send_mail
from django.conf import settings


def send_order_email(order):

    subject = f"🛒 New Order Received - #{order.id}"

    message = f"""
New Order Received

Order ID:
{order.id}

Customer:
{order.customer_name}

Mobile:
{order.mobile}

Products:
{order.products}

Amount:
₹{order.total_amount}

UTR Number:
{order.utr_number}

Address:
{order.address}

Payment Status:
{order.payment_status}

Order Time:
{order.created_at}
"""

    send_mail(

        subject,

        message,

        settings.EMAIL_HOST_USER,

        [settings.EMAIL_HOST_USER],

        fail_silently=False

    )