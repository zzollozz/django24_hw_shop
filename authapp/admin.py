from django.contrib import admin

from authapp.models import Client


class ClientAdmin(admin.ModelAdmin):

    list_display = ['name', 'registration_date']
    ordering = ['registration_date']
    search_fields = ['registration_date']
    search_help_text = 'Поиск по имени'

    readonly_fields = ['registration_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            }
        ),
        (
            'Дата регистрации',
            {
                'classes': ['wide'],
                'fields': ['registration_date']
            }
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'fields': ['email', 'phone_number', 'address']
            }
        ),

    ]






admin.site.register(Client, ClientAdmin)