import requests

TOKEN="EAAOKZBCNUGLMBRz6yZCSWwD4pHHRpw7ZAHKLLaZBh2KeQfqy4g7eqFutmdYoOjg8wfFrRkVXryZBUH3AAdKr2TXxOpFpCflQDI39WqagrV4PghY7uxcvPptpfEz8Y3GqJNrYICXXbPgaDcrZBOZAoAzrPYMi5nHwF7N91P8FVaU2jjXYc3Ly4cNCAVnzTDjTuBEZBgZDZD"

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