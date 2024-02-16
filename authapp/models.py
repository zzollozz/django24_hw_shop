from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100, verbose_name='email')
    phone_number = models.PositiveIntegerField(verbose_name='номер телефона')
    address = models.TextField(verbose_name='адрес регистрации')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='дата регистрации')

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
