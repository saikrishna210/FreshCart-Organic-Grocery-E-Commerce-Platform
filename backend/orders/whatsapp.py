import requests

TOKEN="EAAOKZBCNUGLMBRwhbyZBqMX2nA9Nv0euOgHZBoIOCWmulzvEClkxLf7nW4ZB1qmUTyp9Dqo0XZAWvr7aALsFxOSJtCm0ui5N5hZBfc7dRXlE7RSRAYSoG4ox1MsDauiPlWvohG0JaX1FCQ5QVavlgexxZAplTxsWwDOBPyMmaxY1YWwSrBh8DQ2W7wxP7IvExvvZBgZDZD"

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