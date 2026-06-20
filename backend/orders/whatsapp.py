import requests
TOKEN="EAAOKZBCNUGLMBR7jKt8iPppwgz2ozX1ZCphv0ak8Ul3LuDwRlbwReOuadO6P6L94oZAjZADTPo566awREylhzKfa8zG10MWg36ZA9Vaonm4hiRaoazmSBrOmIVG6TH6bU1bCTa7n9zCwrMV9uwtZACig5cCr6dOPyZAdkJ4i8ZA8hE5qrMm6WZAF7T80h514h4wpb5f4wV2QBaE9K1cAQoU03vbp1UGLaZCVOZCkoB2VJklZCXIovvz1DKWvKBZA158EfUz7KjbvZBuxZAGBZCJIuaSSmW43WahWmgZDZD"
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