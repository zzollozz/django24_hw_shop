from django.core.validators import MinValueValidator
from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Название')
    description = models.TextField(null=True, default=None, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена', validators=[MinValueValidator(0)])
    quantity = models.IntegerField(default=0, verbose_name='Количество', validators=[MinValueValidator(0)])
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    img_product = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
