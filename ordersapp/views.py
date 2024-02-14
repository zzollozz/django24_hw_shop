from datetime import date, timedelta

from django.shortcuts import render, get_object_or_404

from ordersapp.models import Order, OrderCard
from authapp.models import Client


def order_read(request, user_id=None):
    if user_id:
        user = get_object_or_404(Client, pk=user_id)
        start_dates = [date.today() - timedelta(days=d) for d in [7, 30, 365]]
        all_user_orders = Order.objects.filter(user_id=user.id)

        orders_day = [item.good_id.only()[0].name for item in all_user_orders.filter(order_date__gte=start_dates[0])]
        orders_month = [item.good_id.only()[0].name for item in all_user_orders.filter(order_date__gte=start_dates[1])]
        orders_year = [item.good_id.only()[0].name for item in all_user_orders.filter(order_date__gte=start_dates[2])]

        context = {
            'title': f'заказы: {user.name}',
            'user': user.name,
            'orders_day': orders_day,
            'orders_month': orders_month,
            'orders_year': orders_year
        }
        return render(request, 'ordersapp/read_client_order.html', context)
    else:
        orders = [order.good_id.get() for order in Order.objects.all()]

        context = {
            'title': 'Все заказы',
            'orders': orders
        }
        return render(request, 'ordersapp/read_orders.html', context)
