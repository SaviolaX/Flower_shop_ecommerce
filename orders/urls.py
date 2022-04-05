from unicodedata import name
from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('cart/', views.order, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('add_item/<slug:slug>/', views.add_to_cart, name='add_item'),
    path('remove_item/<int:id>/', views.remove_item, name='remove_item'),
    
]