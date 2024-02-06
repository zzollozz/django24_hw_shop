import json
from random import choices

from django.core.management.base import BaseCommand

from ordersapp.models import Order
from authapp.models import Client
from mainapp.models import Goods
from project_Schop import settings


class Command(BaseCommand):
    help = '''
    Создание фейковый данных в базе
    пример:
        python manage.py create_fake_data_db 5
    5 - может любое число (количество клиентов)
    количество заказов посчитывается  (количество клиентов * количество клиентов)
    '''

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='quantity_users')

    def handle(self, *args, **kwargs):
        # Добавление клиентов в базу
        Client.objects.all().delete()
        Client.objects.bulk_create(self.create_users(kwargs.get('count')))

        # Добавление продуктов в базу
        Goods.objects.all().delete()
        Goods.objects.bulk_create(self.add_products('test_products.json'))

        # Создание заказов
        Order.objects.all().delete()

        count_order = kwargs.get('count') * kwargs.get('count')
        clients = [user.id for user in Client.objects.all()]
        products = Goods.objects.all()

        for _ in range(count_order):
            product = choices(products, k=1)[0]
            order = Order.objects.create(
                user_id=Client.objects.filter(pk=int(choices(clients, k=1)[0]))[0],
                all_sum_order=product.price
            )
            order.good_id.add(product)


    @staticmethod
    def create_users(count):
        clients = []

        for i in range(1, count + 1):
            clients.append(
                Client(name=f'fake_User_{i}',
                       email=f'fake_user{i}@example.com',
                       phone_number=int(f'7900{i}{i}{i}2200'),
                       address=f'город{i}, улица{i}')
            )
        return clients

    @staticmethod
    def add_products(file_name: str):
        with open(f"{settings.BASE_DIR}/mainapp/json/{file_name}") as file:
            data = json.load(file)
        product_list = []

        for item in data: #self._load_data_from_file('test_products.json'):
            product_list.append(
                Goods(
                    name=item.get('name'),
                    description=item.get('description'),
                    price=item.get('price'),
                    quantity=item.get('quantity')
                )
            )
        return product_list


