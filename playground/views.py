from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg

from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order


# Create your views here.
def say_hello(request):
    result = Product.objects.aggregate(count=Count("id"),minprice=Min('unit_price'))
    return render(request, "hello.html", {"name": "Siwar", "result": result})
