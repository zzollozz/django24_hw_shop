from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return HttpResponse('форма входа в аккаунт')

def logout(request):
    return HttpResponse('ф-я выхода из аккаунта')

def register(request):
    return HttpResponse('форма регистрации')

def edit(request):
    return HttpResponse('форма редактирования')