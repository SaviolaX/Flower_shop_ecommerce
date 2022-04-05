from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='product_categories'),
    path('category/<slug:slug>/', views.products, name='products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]