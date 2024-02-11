from django.urls import path, include

import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('read/<int:user_id>', ordersapp.order_read, name='order_read'),
    path('read/', ordersapp.order_read, name='order_read'),
]