from django.core.validators import MinValueValidator
from django.db import models
from mainapp.models import Goods
from authapp.models import Client


class Order(models.Model):
    """Заказы клиентов магазина."""
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    good_id = models.ManyToManyField(Goods, through='OrderCard')
    all_sum_order = models.DecimalField(max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'№ {self.pk} - {self.order_date.date()}'
        # return f"{self.user_id}, {self.good_id}, {self.all_sum_order}"

    class Meta:
        verbose_name = ' заказ'
        verbose_name_plural = 'заказы'


class OrderCard(models.Model):
    """Количественный состав заказа по продуктам."""
    good_id = models.ForeignKey(Goods, on_delete=models.PROTECT)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.order_id.good_id}. {self.good_id.name} - {self.product_count}'

    class Meta:
        verbose_name = 'ордер заказа'
        verbose_name_plural = 'ордер заказов'
