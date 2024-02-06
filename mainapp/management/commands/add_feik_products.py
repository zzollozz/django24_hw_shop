import json

from django.core.management.base import BaseCommand

from mainapp.models import Goods
from project_Schop import settings


class Command(BaseCommand):
    help = 'Заполнение фейковыми продуктами'

    @staticmethod
    def _load_data_from_file(file_name):
        """ Метод загрузки данных из файла """
        with open(f"{settings.BASE_DIR}/mainapp/json/{file_name}") as file:
            return json.load(file)

    def handle(self, *args, **kwargs):
        Goods.objects.all().delete()
        product_list = []

        for item in self._load_data_from_file('test_products.json'):
            product_list.append(
                Goods(
                    name=item.get('name'),
                    description=item.get('description'),
                    price=item.get('price'),
                    quantity=item.get('quantity')
                )
            )

        Goods.objects.bulk_create(product_list)  # пакетная вставка
