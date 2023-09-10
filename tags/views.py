from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer, Collection
from django.db.models.fields import DecimalField
from tags.models import ContentType, TaggedItem


# Create your views here.
def say_hello(request):
    # collection = Collection(pk=11)
    # collection.featured_product = None
    # collection.save()

    Collection.objects.filter(pk=11).update(featured_product=None)

    return render(request, "hello.html", {"name": "Siwar"})
