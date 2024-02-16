from django.contrib import admin

from mainapp.models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    list_filter = ['name', 'price']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
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


admin.site.register(Goods, GoodsAdmin)

