from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


# Create your views here.
def say_hello(request):
    exists = Product.objects.filter(pk=0).exists() 
    return render(request, "hello.html", {"name": "Siwar"})
