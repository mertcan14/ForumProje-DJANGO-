from django.contrib import admin
from django.urls import path, include
from .views import anaSayfa, kayitSoru, detail, SoruBegen, SoruBegenSil, yorumlarUser, yorumSil, yorumUpdate, sorularUser, soruUpdate, soruSil, arkadaslariminSorulari
urlpatterns = [
    path('', anaSayfa, name="AnaSayfa"),
    path('arkadaslarimin/', arkadaslariminSorulari, name="arkadaslariminSorulari"),
    path('kategori/<int:id>', anaSayfa, name="AnaSayfaKategori"),
    path('detail/<slug:slugg>', detail, name="detailSoru"),
    path('kayitSoru/', kayitSoru, name="kayitSoru"),


    path('soruUpdate/<slug:slugg>', soruUpdate, name="soruUpdate"),
    path('soruSil/<slug:slugg>', soruSil, name="soruSil"),
    path('sorularUser/', sorularUser, name="sorularUser"),

    path('yorumlarUser/', yorumlarUser, name="yorumlarUser"),
    path('yorumSil/<int:id>', yorumSil, name="yorumSilSoru"),
    path('yorumUpdate/<int:id>', yorumUpdate, name="yorumUpdateSoru"),

    path('begen/<slug:slugg>', SoruBegen, name="begenSoru"),
    path('begenSil/<slug:slugg>', SoruBegenSil, name="begensilSoru"),
    
]
