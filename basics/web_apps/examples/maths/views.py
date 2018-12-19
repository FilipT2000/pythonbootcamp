# django QuerySets

from django.shortcuts import render

# Create your views here.

from django.contrib import admin

from django.http import HttpResponse

from django.urls import path

from maths.models import Math


def obliczenia(request, modul,x,y):
    x, y = int(x), int(y)

    m = Math(operacja=modul, a=x, b=y, wynik=wynik)
    m.save()

    print(m.a, m.b, m.operacja)


    if modul =='add':
        wynik = int(x) + int(y)
        return HttpResponse(f"Wynik: {int(x)+int(y)}")
    if modul == 'sub':
        wynik = int(x)-int(y)
        return HttpResponse(f"Wynik: {int(x)-int(y)}")
    if modul == 'div':
        if int(y)==0:
            return HttpResponse(f"Dzielenie przez 0 :///")
        else:
            wynik = int(x)/int(y)
            return HttpResponse(f"Wynik: {int(x)/int(y)}")
    if modul == 'mul':
        wynik = int(x)*int(y)
        return HttpResponse(f"Wynik: {int(x)*int(y)}")
    # else:
    #     return HttpResponse(f"Nie ma takiej komendy. Możesz wpisać: /add /sub /mul / div")
    else:
        return HttpResponse(f"A kuku")
