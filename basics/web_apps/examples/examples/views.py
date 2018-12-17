# python manage.py startapp maths


from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def hello(request, imie=""):
    if not imie:
        imie = 'World'
    return HttpResponse(f"Hello {imie}")

