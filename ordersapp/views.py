from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from mainapp.models import Goods
from ordersapp.models import Order

# это заглушка на будущее
class OrderCreate(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:orders_list')

class OrderUpdate(UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:orders_list')

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:orders_list')

class OrderRead(DetailView):
    model = Order
    extra_context = {'title': 'заказы/просмотр'}

def get_product_price(request, pk):
    # breakpoint()
    product = Goods.objects.filter(pk=int(pk)).first()
    if product:
        return JsonResponse({'price': product.price})
    else:
        return JsonResponse({'price': 0})
