from django.shortcuts import render
from django.conf import settings
import os
import json
# Create your views here.


def main(request):
    content = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {
        'title': 'Продукты',
        'links_menu': links_menu
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
