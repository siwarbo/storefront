from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.fields import DecimalField
from tags.models import TaggedItem, ContentType
from store.models import Product, Collection


# Create your views here.
def say_hello(request):
    collection = Collection()
    collection.title = "Video Games"
    collection.featured_product = Product(pk=1)
    collection.save()
    collection.id
    # collection = Collection(pk=11)

    # collection.featured_product = None
    # collection.save()

    Collection.objects.filter(pk=11).update(featured_product=None)

    return render(request, "hello.html", {"name": "Rami"})
