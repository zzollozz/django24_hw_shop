from random import choices

from django.core.management.base import BaseCommand

from ordersapp.models import Order
from authapp.models import Client
from mainapp.models import Goods


class Command(BaseCommand):
    help = "Заполнение тест заказами базы"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="количество заказов")

    def handle(self, *args, **options):
        Order.objects.all().delete()

        count = options.get('count')
        clients = [user.id for user in Client.objects.all()]
        products = Goods.objects.all()
        for _ in range(count):
            product = choices(products, k=1)[0]
            order = Order.objects.create(
                user_id=Client.objects.filter(pk=int(choices(clients, k=1)[0]))[0],
                all_sum_order=product.price
            )
            order.good_id.add(product)




