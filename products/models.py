from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
    SUGAR_CHOICES = [
        ('0', '0%'),
        ('30', '30%'),
        ('50', '50%'),
        ('70', '70%'),
        ('100', '100%'),
    ]
    ICE_CHOICES = [
        ('low', 'Ít đá'),
        ('medium', 'Vừa'),
        ('high', 'Nhiều'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    calories = models.IntegerField()
    ingredients = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Tùy chỉnh
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='M')
    sugar = models.CharField(max_length=3, choices=SUGAR_CHOICES, default='50')
    ice = models.CharField(max_length=10, choices=ICE_CHOICES, default='medium')

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ProductTopping(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'