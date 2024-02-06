from django.core.management.base import BaseCommand
from authapp.models import Client

class Command(BaseCommand):
    help = 'Создание фейковый Клиентов в базе'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='quantity_users')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'fake_User_{i}',
                            email=f'fake_user{i}@example.com',
                            phone_number=int(f'7900{i}{i}{i}2200'),
                            address=f'город{i}, улица{i}')
            client.save()
