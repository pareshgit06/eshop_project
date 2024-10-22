from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('add_to_cart<int:id>', views.add_to_cart, name='add_to_cart'),
    path('increment<int:id>', views.increment, name='increment'),
    path('decrement<int:id>', views.decrement, name='decrement'),
    path('delet_item<int:id>', views.delet_item, name='delet_item'),
    path('contact', views.contact, name='contact'),
    path('detail<int:id>', views.detail, name='detail'),
    path('fackdetail', views.fackdetail, name='fackdetail'),
    path('shop/', views.shop, name='shop'),
    path('checkout', views.checkout, name='checkout'),
    path('login', views.login, name='login'),
    path('log_out', views.log_out, name='log_out'),
    path('register', views.register, name='register'),
    path('forgot', views.forgot, name='forgot'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('remove_wishlist/<int:id>/', views.remove_wishlist, name='remove_wishlist'),
    path('add_to_wishlist/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),


    

    
]