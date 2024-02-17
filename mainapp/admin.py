from django.contrib import admin
from django.utils.safestring import mark_safe

from mainapp.models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'img_prev', 'price', 'quantity']
    list_filter = ['name', 'price']
    readonly_fields = ['img_prev']
    save_on_top = True

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Изображение',
            {
                'fields': ['img_product'],
            }
        ),
        (
            None,
            {
                'fields': ['img_prev'],
            }
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price']
            }
        ),
        (
            'Склад',
            {
                'fields': ['quantity'],
            }
        ),
    ]

    @admin.display(ordering='name', description='фото товара')
    def img_prev(self, goods: Goods):
        if goods.img_product:
            return mark_safe(
                f'<img src="{goods.img_product.url}" style="width: 50px; height: auto;" alt="Изображения нет">')
        return f"без фото"

admin.site.register(Goods, GoodsAdmin)

