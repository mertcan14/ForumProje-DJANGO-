from django.contrib import admin
from django.urls import path, include
from .views import arkadasIstek, arkadaslikIstekListe, arkadasKabul, arkadasListem, arkadasIstekSil, arkadasSil, arkadasIstekIptal
urlpatterns = [
    path('istekArkadas/<int:id>', arkadasIstek, name="arkadasIstek"),
    path('arkadasIstek/', arkadaslikIstekListe, name="arkadaslikIstekListe"),
    path('arkadasKabul/<int:id>', arkadasKabul, name="arkadasKabul"),
    path('arkadasIstekSil/<int:id>', arkadasIstekSil, name="arkadasIstekSil"),
    path('arkadasSil/<int:id>', arkadasSil, name="arkadasSil"),
    path('arkadasIstekIptal/<int:id>', arkadasIstekIptal, name="arkadasIstekIptal"),
    path('arkadaslarim/', arkadasListem, name="arkadasListem"),
]