from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order, Customer


# Create your views here.
def say_hello(request):
    query_set = Customer.objects.annotate(
        full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    )
    query_set = Customer.objects.annotate(
        full_name=Concat("first_name", Value(" "), "last_name")
    )

    return render(request, "hello.html", {"name": "Siwar", "result": list(query_set)})
