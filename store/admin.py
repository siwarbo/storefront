from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Count
from django.http.request import HttpRequest
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_per_page = 10
    list_select_related = ["collection"]

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        return "OK"


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "payment_status", "customer"]
    list_editable = ["payment_status"]
    ordering = ["id"]
    list_per_page = 10
    list_select_related = ["customer"]

    def customer_id(self, order):
        return order.customer_id


# @admin.register(models.Collection)
# class CollectionAdmin(admin.ModelAdmin):
#     list_display = ["title", "products_count"]

#     def products_count(self, collection):
#         return collection.products_count

#     def get_queryset(self, request):
#         return super().get_queryset(request).annotate(products_count=Count("product"))


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    list_per_page = 10


admin.site.register(models.Collection)
