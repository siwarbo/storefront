from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer, Collection
from django.db.models.fields import DecimalField
from tags.models import ContentType, TaggedItem


# Create your views here.
def say_hello(request):
    collection = Collection()
    collection.title = "Video Games"
    collection.featured_product = Product(pk=1)
    collection.save()
    collection.id

    return render(request, "hello.html", {"name": "Siwar"})
