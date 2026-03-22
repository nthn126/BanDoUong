from django.db import models
from django.contrib.auth.models import User
from products.models import Product, Topping

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart of {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=1, default='M')
    sugar = models.CharField(max_length=3, default='50')
    ice = models.CharField(max_length=10, default='medium')
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f'{self.product.name} x{self.quantity}'

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Chờ xác nhận'),
        ('preparing', 'Đang chuẩn bị'),
        ('delivering', 'Đang giao hàng'),
        ('delivered', 'Đã giao'),
        ('cancelled', 'Đã hủy'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    payment_method = models.CharField(max_length=50)  # COD, Momo, etc.

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá tại thời điểm đặt
    size = models.CharField(max_length=1, default='M')
    sugar = models.CharField(max_length=3, default='50')
    ice = models.CharField(max_length=10, default='medium')
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f'{self.product.name} x{self.quantity}'