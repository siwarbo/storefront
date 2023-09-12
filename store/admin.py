from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count
from django.http.request import HttpRequest
from django.utils.html import format_html, urlencode
from django.urls import reverse
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

#     @admin.display(ordering="products_count")
#     def products_count(self, collection):
#         url = (
#             reverse("admin:store_product_changelist")
#             + "?"
#             + urlencode({"collection__id": str(collection.id)})
#         )
#         return format_html('<a href="{}">{}</a>', url, collection.products_count)

#     def get_queryset(self, request):
#         return super().get_queryset(request).annotate(products_count=Count("product"))


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    list_per_page = 10
    search_fields = ["first_name__istartswith", "last_name__istartswith"]


admin.site.register(models.Collection)
