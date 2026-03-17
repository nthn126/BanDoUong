from django.contrib import admin
from .models import Category, Product, Topping, ProductTopping, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_available']
    list_filter = ['category', 'is_available']

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']