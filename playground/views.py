from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


# Create your views here.
def say_hello(request):
    query_set = Product.objects.filter(title__icontains ="coffee")
    return render(request, "hello.html", {"name": "Siwar", "products": list(query_set)})
