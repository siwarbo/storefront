from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer
from django.db.models.fields import DecimalField
from tags.models import ContentType, TaggedItem


# Create your views here.
def say_hello(request):
    content_type = ContentType.objects.get_for_model(Product)
    query_set = TaggedItem.objects.select_related("tag").filter(
        content_type=content_type, object_id=1
    )

    return render(request, "hello.html", {"name": "Siwar", "tags": list(query_set)})
