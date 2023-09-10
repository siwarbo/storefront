from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.fields import DecimalField
from django.db import transaction, connection
from tags.models import TaggedItem, ContentType
from store.models import Product, Collection, Order, OrderItem


# Create your views here.
def say_hello(request):
    with transaction.atomic():
        with connection.cursor() as cursor:
            cursor.callproc("get_customers", [1, 2, 'a'])

    return render(request, "hello.html", {"name": "Siwar"})
