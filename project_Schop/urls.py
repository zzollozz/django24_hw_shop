"""
Конфигурация URL-адреса для проекта project_Schop.

Список `urlpatterns` направляет URL-адреса в представления. Для получения дополнительной информации см.:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Примеры:
Представления функций
    1. Добавьте импорт: из представлений импорта my_app.
    2. Добавьте URL-адрес в urlpatterns: path('',views.home, name='home')
Представления на основе классов
    1. Добавляем импорт: fromother_app.views import Home
    2. Добавьте URL-адрес в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf
    1. Импортируйте функцию include(): из django.urls import include, путь
    2. Добавьте URL-адрес в urlpatterns: path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from project_Schop import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='adminapp'),
    path('', include('mainapp.urls', namespace='mainapp')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('orders/', include('ordersapp.urls', namespace='orders')),
    path('__debug__/', include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
