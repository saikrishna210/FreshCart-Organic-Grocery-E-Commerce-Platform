import razorpay
from django.conf import settings


client=razorpay.Client(
    auth=(
        settings.RAZOR_KEY,
        settings.RAZOR_SECRET
        )
)


def create_order(amount):

    data={

        "amount":
        int(amount*100),

        "currency":
        "INR",
    }

    return client.order.create({
        "amount":int(amount*100),
        "currency":"INR",
        "payment_capture":1
    })