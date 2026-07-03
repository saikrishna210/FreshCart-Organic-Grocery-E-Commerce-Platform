from django.urls import path
from . import views

urlpatterns=[
path('',views.home),
path('ghee_oil/',views.ghee_oil),
path('seeds_dryfruits/',views.seeds_dryfruits),
path('pulses_dal/',views.pulses_dal),
path('grains_cereals/',views.grains_cereals),
path('rice_millets/',views.rice_millets),
path('fruits/',views.fruits),
path('sweet_salts/',views.sweet_salts),
path('snacks/',views.snacks),
path('',views.home,name='home'),
path('over_story/',views.over_story),
path('happy_farmers/',views.happy_farmers),
path('offers/',views.offers),
path('giving_back/',views.giving_back),
path('contact_us/',views.contact_us),
path('mangoes/',views.mangoes),
path('vegetables/',views.vegetables),
path('juices/',views.juices),
path('kitchen_essentails/',views.kitchen_essentails),
path('rice_millets/',views.rice_millets),
path('save-order/',views.save_order),
path("success/",views.success),
]