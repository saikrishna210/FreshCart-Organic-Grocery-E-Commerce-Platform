import requests
TOKEN="EAAOKZBCNUGLMBRmvOOvsoZAlyaHZAez2L0TENEQirOSoRZCUTX9n1tkqTQ97pUi07Y6q2RZCZASOLKix98K61LGQOlhsWzBe68o42AaZBp98VAGNEohqEImMySLZBj1aJk2Vm7VatFS05UkWwoVHFuROuw5yKeFDRjhLhz25EBZCDb0NPYHHIeMTDjZBe8Fec4xQmvYUkiDp551UIZA8dm7wyNWZCJrmNQLw9FQY9lBvTYG1SusLZAPlQiEJdZCM4D3K2URrzj0wtkVUTR6JZCIK6pEaKcm7ccvvQZDZD"
PHONE_ID="1188781930979463"
def send_whatsapp(phone,msg):
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
    payload={
        "messaging_product":"whatsapp",
        "to":phone,
        "type":"template",
        "template":{
            "name":"hello_world",
            "language":{
                "code":"en_US"
            }
        }
    }
    response=requests.post(
        url,
        json=payload,
        headers=headers
    )
    print(response.text)