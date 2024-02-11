from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    img_product = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return f"Заказ: {self.name}, количество: {self.quantity}"

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
