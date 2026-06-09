import requests
TOKEN="EAAOKZBCNUGLMBRtGZBwCE6WA4slHtHJKjlW2vwidC0z78s3NCcKY900vZC1rDAL2gbNAN6xeAmfEQaiCXPqOxIo5BrV8ZBjDmeOZCZBO9Nknuh6V2LKcjCDP5z3xpBzu0LiQ181axu12ENzEB4BV7AAwdciBsIQ5Vo9FHYAs9sjQuPvY5JVl2j7ugi3wkVobcdZBvUTlOhliknbJ16Rl9K5841yCoNyZApS1ZCmIBIR3xQiXyjxyOa9HY1V0SvoZAFZBl13i5lTZBIuCZANuVuzTzbJEEhWYP"
PHONE_ID="1188781930979463"

def send_whatsapp(phone,msg):
    url=f"https://graph.facebook.com/v23.0/{PHONE_ID}/messages"
    headers={
        "Authorization":f"Bearer {TOKEN}",
        "Content-Type":"application/json"
    }
    payload={
        "messaging_product":"whatsapp",
        "to":"919640546718",
        "type":"template",
        "template":{
            "name":"orderconfirmation",
            "language":{
                "code":"en_US"
            },
            "components":[
                {
                    "type":"body",
                    "parameters":[
                        {"type":"text","text":str(msg["id"])},
                        {"type":"text","text":msg["customer"]},
                        {"type":"text","text":msg["products"]},
                        {"type":"text","text":str(msg["amount"])},
                        {"type":"text","text":msg["utr"]},
                        {"type":"text","text":msg["address"]}
                    ]
                }
            ]
        }
    }
    response=requests.post(
        url,
        json=payload,
        headers=headers
    )
    print("STATUS:",response.status_code)
    print("RESPONSE:",response.text)
