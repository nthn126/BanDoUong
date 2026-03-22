from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, Cart, CartItem
from products.models import Product

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.cartitem_set.all()
    total = sum(item.product.price * item.quantity for item in items)
    return render(request, 'orders/cart.html', {'cart': cart, 'items': items, 'total': total})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    size = request.POST.get('size', 'M')
    sugar = request.POST.get('sugar', '50')
    ice = request.POST.get('ice', 'medium')
    item, created = CartItem.objects.get_or_create(
        cart=cart, 
        product=product, 
        size=size, 
        sugar=sugar, 
        ice=ice,
        defaults={'quantity': 1}
    )
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f'Đã thêm {product.name} vào giỏ hàng.')
    return redirect('product_detail', pk=product_id)

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.cartitem_set.all()
    if not items:
        messages.error(request, 'Giỏ hàng trống.')
        return redirect('cart')
    if request.method == 'POST':
        shipping_address = request.POST['shipping_address']
        payment_method = request.POST['payment_method']
        total_price = sum(item.product.price * item.quantity for item in items)
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            shipping_address=shipping_address,
            payment_method=payment_method
        )
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
                size=item.size,
                sugar=item.sugar,
                ice=item.ice
            )
        cart.cartitem_set.all().delete()  # Xóa giỏ hàng
        messages.success(request, 'Đặt hàng thành công!')
        return redirect('order_detail', pk=order.id)
    return render(request, 'orders/checkout.html', {'items': items, 'total': sum(item.product.price * item.quantity for item in items)})