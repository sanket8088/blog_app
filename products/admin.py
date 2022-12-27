from django.contrib import admin
from products.models import Categories, Products

# Register your models here.

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]

