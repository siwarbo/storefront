from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F

from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


# Create your views here.
def say_hello(request):
    product = Product.objects.order_by('unit_price')[0]
    product = Product.objects.latest('unit_price')

    return render(request, "hello.html", {"name": "Siwar", "product": product})
