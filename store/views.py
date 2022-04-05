from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from payment.tasks import send_email


def index(request):

    context = {}
    return render(request, 'index.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, product_slug=slug)

    context = {'product': product}
    return render(request, 'store/product_detail.html', context)


def products(request, slug):
    category = get_object_or_404(Category, category_slug=slug)
    products = Product.objects.filter(product_category=category)

    context = {'products': products, 'category': category}
    return render(request, 'store/products.html', context)


def categories(request):
    categories = Category.objects.all()

    context = {'categories': categories}
    return render(request, 'store/categories.html', context)
