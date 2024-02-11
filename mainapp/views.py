import logging

from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect

from mainapp.forms import AddProductForm
from mainapp.models import Goods

logger = logging.getLogger(__name__)


def index(request):
    context = {
        'title': 'главная страница',
        'name_content': 'Стартовая страница магазина'
    }
    return render(request, 'mainapp/index.html', context)


def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)

        if form.is_valid():
            item_product = Goods(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                quantity=form.cleaned_data['quantity'],
                img_product=form.cleaned_data['img_product']
            )
            item_product.save()
            logger.info(f"Создали продукт {item_product.name=}, в колличестве {item_product.quantity=}")

        return HttpResponseRedirect(reverse('mainapp:home'))
    else:
        form = AddProductForm()

    context = {
        'title': 'форма добавления продукта',
        'name_content': 'Добавление нового продукта в базу ',
        'form': form
    }

    return render(request, 'mainapp/add_product.html', context)
