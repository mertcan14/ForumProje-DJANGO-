from django.shortcuts import render, get_object_or_404
from Forum.views import userNotLogged
from .models import ArkadasIstek, Arkadasım
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q

def arkadasIstekKontrol(atan, alan):
    if atan == alan:
        return "Aynı kullanici"
    atall1 = str(atan) + str(alan)
    atall2 = str(alan) + str(atan)
    kontrol = ArkadasIstek.objects.filter(atal = atall1).count()
    arkadasKontrol = Arkadasım.objects.filter(Q(arkadas1_2=atall1) | Q(arkadas1_2=atall2)).count()
    istekKontrol = ArkadasIstek.objects.filter(atal = atall2).count()
    if arkadasKontrol != 0:
        return "Arkadaslitan cikar"
    elif kontrol == 0:
        if istekKontrol != 0:
            return "istek kabulOrRed"
        return "istek atabilir"
    else:
        return "istek iptal"


@userNotLogged
def arkadasIstek(request, id):
    try:
        istek = arkadasIstekKontrol(request.user.id, id)
        atal = str(request.user.id) + str(id)
        if istek == "istek atilamaz":
            messages.warning(request, "Zaten istek gönderilmiş")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        elif istek == "Aynı kullanici":
            messages.warning(request, "Kendinize istek gönderemezsiniz.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            alanKullanici = get_object_or_404(User, id = id)
            istekk = ArkadasIstek(atal = atal, alanKullanici = alanKullanici, atanKullanici = request.user)
            istekk.save()
            messages.success(request, "Başarı ile istek iletildi...")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except:
        messages.warning(request, "Hata oluştu.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

@userNotLogged
def arkadaslikIstekListe(request):
    istekler = ArkadasIstek.objects.filter(alanKullanici = request.user)
    isteklerr = ArkadasIstek.objects.filter(alanKullanici = request.user).count()
    if isteklerr == 0:
        istekler = None
    context={
        "istekler":istekler,
    }
    return render(request, "Arkadas/arkadaslikIstekler.html", context)

@userNotLogged
def arkadasKabul(request, id):
    try:
        kontrol = ArkadasIstek.objects.get(alanKullanici=request.user, atanKullanici=id)
        if kontrol is None:
            messages.warning(request, "Arkadaşlık isteği bulunamadı..")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        newFriend = Arkadasım(arkadas1_2=kontrol.atal, arkadas1 = kontrol.atanKullanici, arkadas2 = request.user)
        newFriend.save()
        kontrol.delete()
        messages.success(request, "Başarı ile kabul edildi")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    except:
        messages.warning(request,"İstenmeyen bir hata oluştu")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

@userNotLogged
def arkadasIstekSil(request, id):
    try:
        kontrol = ArkadasIstek.objects.get(alanKullanici=request.user, atanKullanici=id)
        if kontrol is None:
            messages.warning(request, "Arkadaşlık isteği bulunamadı..")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        kontrol.delete()
        messages.success(request, "Başarı ile silindi.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    except:
        messages.warning(request,"İstenmeyen bir hata oluştu")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

@userNotLogged
def arkadasIstekIptal(request, id):
    try:
        kontrol = ArkadasIstek.objects.get(atanKullanici=request.user, alanKullanici=id)
        if kontrol is None:
            messages.warning(request, "Arkadaşlık isteği bulunamadı..")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        kontrol.delete()
        messages.success(request, "Başarı ile silindi.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    except:
        messages.warning(request,"İstenmeyen bir hata oluştu")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 


" ARKADASLARIM "


@userNotLogged
def arkadasListem(request):
    try:
        arkadaslarim = Arkadasım.objects.filter(Q(arkadas1=request.user) | Q(arkadas2=request.user))
        arkadaslarimToplam = Arkadasım.objects.filter(Q(arkadas1=request.user) | Q(arkadas2=request.user)).count()
        if arkadaslarimToplam == 0:
            arkadaslarim = None
        istekler = ArkadasIstek.objects.filter(alanKullanici = request.user)[:5]
        isteklerr = ArkadasIstek.objects.filter(alanKullanici = request.user).count()
        if isteklerr == 0:
            istekler = None
        context={
            "arkadaslarim":arkadaslarim,
            "istekler":istekler,
        }
        return render(request, "Arkadas/arkadaslarim.html", context)
    except:
        messages.warning(request, "Maalesef hata alındı")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

@userNotLogged
def arkadasSil(request, id):
    try:
        kontrol1 = str(request.user.id) + str(id)
        kontrol2 = str(id) + str(request.user.id) 
        silinecekArkadas = Arkadasım.objects.get(Q(arkadas1_2 = kontrol1) | Q(arkadas1_2 = kontrol2))
        if silinecekArkadas is None:
            messages.warning(request, "Arkadas Bulunamadı")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        silinecekArkadas.delete()
        messages.success(request, "Başarı ile silindi.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    except:
        messages.warning(request, "Maalesef hata alındı")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
