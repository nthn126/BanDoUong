import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bandouong.settings')
django.setup()

from products.models import Category, Product, Topping

# Tạo categories
categories = [
    {'name': 'Trà', 'description': 'Các loại trà tươi ngon'},
    {'name': 'Cà Phê', 'description': 'Cà phê pha máy và thủ công'},
    {'name': 'Sinh Tố', 'description': 'Sinh tố trái cây'},
]

for cat_data in categories:
    Category.objects.get_or_create(**cat_data)

# Tạo toppings
toppings = [
    {'name': 'Trân châu đen', 'price': 5000},
    {'name': 'Thạch dừa', 'price': 7000},
    {'name': 'Pudding', 'price': 6000},
]

for top_data in toppings:
    Topping.objects.get_or_create(**top_data)

# Tạo products
products = [
    {
        'name': 'Trà Đá',
        'description': 'Trà đen pha với đá',
        'price': 25000,
        'category': Category.objects.get(name='Trà'),
        'calories': 50,
        'ingredients': 'Trà đen, đường, đá',
        'rating': 4.5,
        'is_available': True,
    },
    {
        'name': 'Cà Phê Đen',
        'description': 'Cà phê đen đậm đà',
        'price': 30000,
        'category': Category.objects.get(name='Cà Phê'),
        'calories': 10,
        'ingredients': 'Cà phê rang, nước',
        'rating': 4.8,
        'is_available': True,
    },
    {
        'name': 'Sinh Tố Bơ',
        'description': 'Sinh tố bơ tươi ngon',
        'price': 35000,
        'category': Category.objects.get(name='Sinh Tố'),
        'calories': 200,
        'ingredients': 'Bơ, sữa, đường',
        'rating': 4.7,
        'is_available': True,
    },
]

for prod_data in products:
    Product.objects.get_or_create(**prod_data)

print("Dữ liệu mẫu đã được tạo!")