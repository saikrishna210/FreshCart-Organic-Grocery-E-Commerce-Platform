import requests

TOKEN="EAAOKZBCNUGLMBR7WOauGU6tu7ppkEXq5JYs6tumTV9XOzAPZCnR8rI0H1aYfqOst6WHx5qXQBjbFiaiLa2keUKMBbLeGniYi0KD1SljmhZCjJI9GAlGnTpNf0F906Lnfl2No1ZCsmBh0ljC3mJnYzXV9By7eB3ExrzwREiWdSNy994qTJp1HQe0fZBUuld3MZC8QZDZD"

PHONE_ID="1223756687468118"


def send_whatsapp(phone,msg):

    phone=str(phone).strip()

    if phone.startswith("+"):
        phone=phone[1:]

    if not phone.startswith("91"):
        phone="91"+phone


    url=(
        f"https://graph.facebook.com/v23.0/"
        f"{PHONE_ID}/messages"
    )

    headers={

        "Authorization":
        f"Bearer {TOKEN}",

        "Content-Type":
        "application/json"

    }


    text=f"""
Order Confirmed ✅

Order ID:
{msg["id"]}

Customer:
{msg["customer"]}

Products:
{msg["products"]}

Amount:
₹{msg["amount"]}

UTR:
{msg["utr"]}

Address:
{msg["address"]}

Thank you for shopping ❤️
"""


    payload={

        "messaging_product":
        "whatsapp",

        "to":
        phone,

        "type":
        "text",

        "text":{

            "preview_url":
            False,

            "body":
            text

        }

    }
    r=requests.post(

        url,

        json=payload,

        headers=headers

    )

    print(
        r.status_code
    )

    print(
        r.text
    )