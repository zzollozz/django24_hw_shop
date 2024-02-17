from django.contrib import admin

from ordersapp.models import Order, OrderCard


class ToppingInline(admin.TabularInline):
    model = OrderCard


@admin.action(description='Что то сделать')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class OrderAdmin(admin.ModelAdmin):
    """ Список заказов """

    list_display = ['id', 'user_id', 'order_date', 'all_sum_order', 'order_details']
    ordering = ['id', '-order_date', 'all_sum_order']
    list_filter = ['order_date', 'all_sum_order']
    search_fields = ['id', 'order_date']
    search_help_text = 'Поиск по Номеру заказа или Дате создания'
    # actions = [reset_quantity]

    inlines = [ToppingInline, ]

    # """Отдельный продукт"""
    # fields = ['user_id']
    readonly_fields = ['order_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['user_id'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['order_date'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['all_sum_order'],
            }
        ),
    ]

    exclude = ('toppings',)

    @admin.display(description="Товары в заказе", ordering='user_id')
    def order_details(self, order: OrderCard):
        return [i.name for i in order.good_id.all()]


admin.site.register(Order, OrderAdmin)
