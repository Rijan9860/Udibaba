from django.urls import path
from udibaba import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', views.home,name='home'),
     path('cart/', views.cart, name='cart')
]