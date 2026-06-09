from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
import json
from .whatsapp import send_whatsapp

def home(request):
    return render(request,"index.html")

def ghee_oil(request):
    return render(request,'ghee_oil.html')

def seeds_dryfruits(request):
    return render(request,'seeds_dryfruits.html')

def pulses_dal(request):
    return render(request,'pulses_dal.html')

def grains_cereals(request):
    return render(request,'grains_cereals.html')

def rice_millets(request):
    return render(request,'rice_millets.html')

def fruits(request):
    return render(request,'fruits.html')

def sweet_salts(request):
    return render(request,'sweet_salts.html')

def snacks(request):
    return render(request,'snacks.html')

def over_story(request):
    return render(request,'over_story.html')

def happy_farmers(request):
    return render(request,'happy_farmers.html')

def offers(request):
    return render(request,'offers.html')

def giving_back(request):
    return render(request,'giving_back.html')

def contact_us(request):
    return render(request,'contact_us.html')

def mangoes(request):
    return render(request,'mangoes.html')

def vegetables(request):
    return render(request,'vegetables.html')

def juices(request):
    return render(request,'juices.html')

def kitchen_essentails(request):
    return render(request,'kitchen_essentails.html')

def rice_millets(request):
    return render(request,'rice_millets.html')

@csrf_exempt
def save_order(request):
    try:
        if request.method=="POST":
            data=json.loads(
                request.body
            )
            order=Order.objects.create(
                customer_name=
                data.get("name"),

                mobile=
                data.get("mobile"),

                address=
                data.get("address"),

                products=
                data.get("products"),

                total_amount=
                float(
                    data.get("amount")
                ),

                utr_number=
                data.get("utr"),

                payment_status=
                "Paid"

            )

            msg={

                "id":
                order.id,

                "customer":
                order.customer_name,

                "products":
                order.products,

                "amount":
                str(
                    order.total_amount
                ),

                "utr":
                order.utr_number,

                "address":
                order.address

            }

            send_whatsapp(

                "919640546718",

                msg

            )

            return JsonResponse({

                "status":
                "success",

                "order_id":
                order.id

            })

        return JsonResponse({

            "status":
            "failed"

        })

    except Exception as e:

        return JsonResponse({

            "status":
            "error",

            "message":
            str(e)

        })

def success(request):
    return render(request,"success.html")

