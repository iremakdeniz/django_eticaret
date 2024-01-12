from django.urls import path
from . import views
from .views import (HomeView, ItemDetailView, OrderSummaryView, AddCouponView, CheckoutView)

app_name = 'spicy'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('index', HomeView.as_view(), name='index'),
    path('login', views.user_login, name="user_login"),
    path('register', views.user_register, name="user_register"),
    path('logout', views.user_logout, name='user_logout'),
    path('checkout', CheckoutView.as_view(), name="checkout"),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', views.remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('cart', OrderSummaryView.as_view(), name="cart"),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),


]

