import requests
TOKEN="EAAOKZBCNUGLMBRnhJjLvgmyiTEwrBSkDaJI0bKo2DPU1CNZAdjWb7kzsGF7pyZAZCPS58G7nZAADvJFy9GwObFMSWwClyl7ezcYFP1mDnzbPX4nGo6fpBqcZBfhM8ndyZBV3wYPq9uDFMJmOlZA3lxtd2hl3PFZCxK3HbwKu02MXw0I8h3hoj6gQXCP1JJAUJmkXqauDBKbiE83VLLY1euKRAgKj7Heg33orgKl9FwnhSKNzLRDANH5veyWQgAraPtMNlZCMZCrRUFjZCphWSZAlwAcSg1p54"
PHONE_ID="1188781930979463"
print(
    "TOKEN EXISTS:",
    bool(TOKEN)
)

print(
    "TOKEN LENGTH:",
    len(TOKEN)
)
def send_whatsapp(phone, msg):

    try:

        phone = str(phone).strip()

        if not phone.startswith("91"):
            phone = "91" + phone

        url = f"https://graph.facebook.com/v23.0/{PHONE_ID}/messages"

        headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }

        payload = {

            "messaging_product": "whatsapp",

            "to": phone,

            "type": "template",

            "template": {

                "name": "orderconfirmation",

                "language": {
                    "code": "en_US"
                },

                "components": [

                    {
                        "type": "body",

                        "parameters":[

{
"type":"text",
"text":str(msg["id"]).replace("\n"," ")
},

{
"type":"text",
"text":msg["customer"].replace("\n"," ")
},

{
"type":"text",
"text":msg["products"].replace("\n"," ")
},

{
"type":"text",
"text":str(msg["amount"]).replace("\n"," ")
},

{
"type":"text",
"text":msg["utr"].replace("\n"," ")
},

{
"type":"text",
"text":msg["address"].replace("\n"," ")
}

]

                           
                    }

                ]

            }

        }

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=30
        )

        print("PHONE:", phone)
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)

        return response.json()

    except Exception as e:

        print("WHATSAPP ERROR:", str(e))