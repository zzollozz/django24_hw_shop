from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='home'),
    path('add/', mainapp.add_product, name='add_product'),
]
