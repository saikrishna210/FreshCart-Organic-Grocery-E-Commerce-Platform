import requests

TOKEN="EAAOKZBCNUGLMBR9kXCkMFiZBKCAePZAMH73zTTPWGCV9kamTB0IZAD7d93C0SBbAxy69xPpZCVil10HWfe9fN2p4EedFuf9qZAlbbQqZCrbZBZANGQ784pjUOTPlThMRMVvGvCVovnKRuG8isoYThr4BooDv3QloOQcMt2UQIqoVK2XZC2ixsZAhRLfpW4VoXNBg2ZBU5AZDZD"

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


    
    print("Status Code:", r.status_code)
    print("Response:", r.text)