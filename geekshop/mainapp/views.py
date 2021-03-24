from django.shortcuts import render
from django.conf import settings
import os
import json
from mainapp.models import Product, ProductCategory
# Create your views here.


def main(request):
    title = 'Главная'
    products = Product.objects.all()[:4]
    content = {
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()[:4]

    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)


def contacts(request):
    locations = []
    with open(os.path.join(settings.BASE_DIR, 'datasets/contacts.json')) as f:
        locations = json.load(f)

    content = {
        'title': 'Контакты',
        'locations': locations
    }
    return render(request, 'mainapp/contact.html', content)
