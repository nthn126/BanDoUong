# TeaVerse - Website bán đồ uống (Django)

Dự án này là một demo website bán đồ uống (TeaVerse) được xây dựng bằng **Django** (Python) với các thành phần chính:

- **Products**: Quản lý sản phẩm, danh mục, topping, đánh giá.
- **Orders**: Quản lý đơn hàng, chi tiết đơn.
- **Users**: Quản lý hồ sơ người dùng, wishlist.
- **Chatbot**: Giao diện chat (chưa tích hợp AI hoàn chỉnh).

---

## 0) Cài đặt trên máy khác (clone + setup)

1. **Clone repo** vào máy mới:

```powershell
git clone <repo-url> bandouong
cd bandouong
```

2. **Tạo môi trường ảo** (khuyến nghị):

```powershell
python -m venv venv
venv\Scripts\activate
```

3. **Cài dependencies**:

```powershell
pip install -r requirements.txt
```

4. **Cấu hình database**:
- Mặc định dùng SQLite (không cần cài thêm).
- Nếu dùng MySQL: cài `mysqlclient`, và chỉnh `bandouong/settings.py` phần `DATABASES`.

5. **Chạy migrations**:

```powershell
python manage.py migrate
```

6. **Tạo tài khoản admin**:

```powershell
python manage.py createsuperuser
```

7. **Chạy server**:

```powershell
python manage.py runserver
```

---

## 1) Chạy dự án

1. Mở terminal vào thư mục gốc:

```powershell
cd C:\Lamthue-1\NguyenNhung-DATN\bandouong
```

2. Cài dependencies (nếu chưa):

```powershell
pip install django
```

3. Chạy migrations:

```powershell
python manage.py migrate
```

4. Tạo tài khoản admin (nếu cần):

```powershell
python manage.py createsuperuser
```

5. Khởi động server:

```powershell
python manage.py runserver
```

6. Truy cập:

- Website: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

---

## 2) Cấu trúc chính (folders)

- `bandouong/` - cấu hình Django và URL chính.
- `products/` - app quản lý sản phẩm + templates.
- `orders/` - app quản lý đơn hàng.
- `users/` - app hồ sơ người dùng.
- `chatbot/` - app giao diện chat (còn rất đơn giản).

### 2.1) Cấu trúc file chính

Dưới đây là cấu trúc chính của dự án; các file quan trọng được ghi chú:

```
bandouong/                    # Project root
├─ bandouong/                 # Django project config
│  ├─ __init__.py
│  ├─ settings.py             # Cấu hình chính (DB, apps, template, static)
│  ├─ urls.py                 # Quy định URL chính (route đến apps)
│  ├─ views.py                # View cho trang chủ (home)
│  └─ wsgi.py
├─ products/                  # App sản phẩm
│  ├─ migrations/             # Migrations auto sinh
│  ├─ admin.py                # Cấu hình admin (hiển thị model trong trang admin)
│  ├─ apps.py
│  ├─ models.py               # Định nghĩa Product, Category, Topping, Review
│  ├─ urls.py                 # Định nghĩa URL cho products
│  ├─ views.py                # Views trả về template
│  └─ templates/products/     # Templates HTML cho products
├─ orders/                    # App đơn hàng
│  ├─ admin.py
│  ├─ models.py               # Order, OrderItem
│  ├─ urls.py
│  ├─ views.py
│  └─ templates/orders/
├─ users/                     # App người dùng
│  ├─ models.py               # UserProfile, Wishlist
│  ├─ urls.py
│  ├─ views.py
│  └─ templates/users/
├─ chatbot/                   # App chatbot
│  ├─ models.py               # ChatMessage, FAQ
│  ├─ urls.py
│  ├─ views.py
│  └─ templates/chatbot/
└─ manage.py                  # Entry point chạy Django
```

### 2.2) Luồng request - workflow cơ bản

1. **Client (browser)** gửi request tới `http://127.0.0.1:8000/`
2. `bandouong/urls.py` định tuyến `''` đến `views.home`
3. `views.home` render template `home.html` (nằm ở `bandouong/templates/home.html`)

Ví dụ với `/products/`:
1. URL `/products/` được định tuyến bởi `bandouong/urls.py` sang `products.urls`
2. Trong `products/urls.py`, `/` gọi `product_list`
3. `product_list` fetch dữ liệu từ `Product.objects.filter(is_available=True)` và render `products/product_list.html`.

---

## 3) Hướng dẫn chỉnh sửa nhanh

### Thêm sản phẩm mới (dùng admin)
1. Đăng nhập `http://127.0.0.1:8000/admin/`
2. Vào mục **Categories** và tạo danh mục.
3. Vào mục **Products** để thêm đồ uống (cần upload ảnh).

### Hiển thị sản phẩm lên trang chính
- Trang `http://127.0.0.1:8000/products/` đã hiện danh sách sản phẩm.
- Template: `products/templates/products/product_list.html`

### Chỉnh sửa giao diện
- Template chung: `bandouong/templates/home.html`
- Mỗi app có folder templates riêng.

---

## 4) Mở rộng / triển khai AI Chatbot

- Hiện tại chat chỉ là giao diện tĩnh tại `chatbot/templates/chatbot/chat.html`.
- Để tích hợp AI (OpenAI / Dialogflow), cần:
  1. Tạo API view trả về response.
  2. Gọi API từ JavaScript của trang chat.

---

## 5) Lưu ý khi chuyển sang MySQL

Nếu muốn dùng MySQL (production):
1. Cài `mysqlclient`.
2. Update `bandouong/settings.py` vào phần `DATABASES`.
3. Chạy lại `python manage.py migrate`.

---

## 6) Tài liệu thêm
- Django docs: https://docs.djangoproject.com/en/4.2/
- Django templates: https://docs.djangoproject.com/en/4.2/topics/templates/
- Django auth: https://docs.djangoproject.com/en/4.2/topics/auth/

---

## 7) Chi tiết code (deep dive)

Dưới đây là phần giải thích sâu hơn để bạn (hoặc bạn của bạn) có thể nắm rõ cách mọi lớp và module phối hợp để tạo ra website.

### 7.1) `bandouong/` (project config)

#### `bandouong/settings.py`
- **INSTALLED_APPS**: định nghĩa app Django sẽ đăng ký (products, orders, users, chatbot + app mặc định như auth, admin...).
- **DATABASES**: hiện dùng SQLite (`db.sqlite3`). Muốn chuyển MySQL thì thay `ENGINE` và các tham số `NAME/USER/PASSWORD/HOST/PORT`.
- **TEMPLATES**: `DIRS` đã cấu hình để Django tìm template ở `bandouong/templates/`.

#### `bandouong/urls.py`
Đây là cổng vào (entrypoint) của web app:
```python
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
    path('chatbot/', include('chatbot.urls')),
]
```
- `include('products.urls')` giúp tách các routes của app `products` ra file riêng.

#### `bandouong/views.py`
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```
- View này chỉ render template `home.html`.

---

### 7.2) App `products/` (quản lý sản phẩm)

#### `products/models.py`
- `Category`: danh mục (ví dụ: Trà sữa, Trà trái cây, Cà phê).
- `Product`: thông tin chi tiết của đồ uống.
  - `Category` là `ForeignKey` (1 danh mục nhiều sản phẩm).
  - `size`, `sugar`, `ice` là các lựa chọn (tùy chỉnh khi khách đặt).
- `Topping`: các loại topping.
- `Review`: đánh giá của user (1 sản phẩm có nhiều đánh giá).

Nếu muốn thêm tính năng mới (ví dụ: `is_featured`):
1. Thêm field vào model.
2. Chạy `python manage.py makemigrations`.
3. Chạy `python manage.py migrate`.

#### `products/views.py`
- `product_list`: lấy tất cả sản phẩm `is_available=True`.
- `product_detail`: lấy chi tiết sản phẩm theo `pk`.

#### `products/urls.py`
```python
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]
```

#### Templates
- `products/templates/products/product_list.html`: hiển thị danh sách sản phẩm.
- `products/templates/products/product_detail.html`: hiển thị chi tiết, bao gồm nguyên liệu, calo, đánh giá.

---

### 7.3) App `orders/` (quản lý đơn hàng)

#### `orders/models.py`
- `Order`: lưu trữ thông tin chung (user, trạng thái, tổng tiền, địa chỉ, phương thức thanh toán).
- `OrderItem`: mỗi sản phẩm trong đơn.

**Luồng đặt hàng cơ bản**:
1. Tạo `Order` mới (status = pending).
2. Tạo `OrderItem` liên kết `order` với từng sản phẩm.
3. Cập nhật `order.total_price` dựa trên tổng giá trị item.

#### `orders/views.py`
- `order_list`: hiển thị đơn hàng của user hiện tại.
- `order_detail`: xem chi tiết một đơn hàng (chỉ của chính user).

#### `orders/urls.py`
```python
urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
]
```

---

### 7.4) App `users/` (quản lý người dùng)

#### `users/models.py`
- `UserProfile`: mở rộng `User` với `phone`, `address`, `date_of_birth`.
- `Wishlist`: lưu sản phẩm yêu thích.

**Ghi chú**: Django có sẵn `User` (username/email/password). `UserProfile` dùng `OneToOneField(User)` để nối thông tin mở rộng.

#### `users/views.py`
- `profile`: render template `users/profile.html` hiển thị thông tin user.

#### `users/urls.py`
```python
urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
```

---

### 7.5) App `chatbot/` (giao diện chat)

#### `chatbot/models.py`
- `ChatMessage`: lưu hội thoại (user message + response).
- `FAQ`: câu hỏi thường gặp.

#### Hiện tại
- `chatbot/views.py` chỉ render `chat.html`.

#### Mở rộng thành AI chatbot
1. Tạo API (ví dụ: `chatbot/api.py`) nhận POST message.
2. Gọi OpenAI (hoặc Dialogflow) trong view.
3. Trả JSON về frontend.
4. Trong `chat.html`, dùng `fetch()` để gửi/nhận và hiển thị.

---

### 7.6) Các bước debug và phát triển nhanh

#### Chạy shell để thử các model
```powershell
python manage.py shell
```
```python
from products.models import Category, Product
c = Category.objects.create(name='Trà sữa')
Product.objects.create(name='Trà sữa trân châu', price=45000, category=c, calories=150, description='...')
```

---

### 7.7) Mở rộng nâng cao (gợi ý)

- Thêm app `cart/` để quản lý giỏ hàng (cart item, checkout).
- Tích hợp thanh toán: Stripe, Momo, hoặc cổng thanh toán khác.
- Tích hợp AI recommendation: Đề xuất sản phẩm dựa trên lịch sử mua hàng.

---