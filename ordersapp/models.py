from django.db import models
from mainapp.models import Goods
from authapp.models import Client

class Order(models.Model):
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    good_id = models.ManyToManyField(Goods)
    all_sum_order = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id}, {self.good_id}, {self.all_sum_order}"

    class Meta:
        verbose_name = ' заказ'
        verbose_name_plural = 'заказы'

