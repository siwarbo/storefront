from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer
from django.db.models.fields import DecimalField
from tags.models import ContentType, TaggedItem


# Create your views here.
def say_hello(request):
    query_set = Product.objects.all()
    list(query_set)
    query_set[0]

    return render(request, "hello.html", {"name": "Siwar", "tags": list(query_set)})
