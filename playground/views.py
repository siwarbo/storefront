from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F

from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem


# Create your views here.
def say_hello(request):
    query_set = Product.objects.defer("description")

    return render(request, "hello.html", {"name": "Siwar", "products": list(query_set)})
