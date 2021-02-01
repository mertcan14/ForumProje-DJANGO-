from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from User.forms import kayitForm, girisForm, profilForms, userForms, resetPasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from passlib.hash import sha256_crypt
from Forum.models import Soru, YorumSoru, BegenSoru
from .models import Profil
from django.utils.dateparse import parse_datetime
import datetime
from Arkadas.views import arkadasIstekKontrol
from Forum.views import userNotLogged


def kayitUser(request):
    form = kayitForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            usernamee = form.cleaned_data.get("username")
            passwordd = form.cleaned_data.get("password")
            emaill = form.cleaned_data.get("email")
            newUser = User(username= usernamee, email= emaill)
            newUser.set_password(passwordd)
            newUser.save()
            login(request, newUser)
            return redirect("kullaniciGiris")
        context ={
            "form": form,
        }
        return render(request, "User/kayit.html", context)
    else:
        form= kayitForm()
        context={
            "form":form,
        }
        return render(request, "User/kayit.html", context)

def girisUser(request):
    form = girisForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            usernamee = form.cleaned_data.get("username")
            passwordd = form.cleaned_data.get("password")
            user = authenticate(username = usernamee, password = passwordd)
            if user is None:
                return redirect("kullaniciGiris")
            login(request, user)
            messages.success(request,"Başarı ile girildi")
            return redirect("AnaSayfa")
        messages.info(request,"Giriş Yapılamadı")
        return redirect("kullaniciKayit")
    context={
        "form":form,
    }
    return render(request, "User/giris.html", context)

@userNotLogged
def cikisUser(request):
    logout(request)
    messages.info(request,"Başarı ile çıkış yapıldı..")
    return redirect("AnaSayfa")


def detailUser(request, id):
    kullanici = get_object_or_404(User, id=id)
    kullaniciProfil =Profil.objects.get(user = kullanici)
    sorular = Soru.objects.filter(reporter = id).order_by("-date")[:5]
    sorularSayi = Soru.objects.filter(reporter = id).count()
    yorumlar = YorumSoru.objects.filter(reporter = id).order_by("-date")[:5]
    yorumlarSayi = YorumSoru.objects.filter(reporter = id).count()
    arkadas = arkadasIstekKontrol(request.user.id, id)
    print(arkadas)
    context={
        "kullanici":kullanici,
        "sorular":sorular,
        "yorumlar": yorumlar,
        "kullaniciProfil": kullaniciProfil,
        "sorularSayi":sorularSayi,
        "yorumlarSayi":yorumlarSayi,
        "arkadas":arkadas,
    }
    return render(request,"User/detailUser.html", context)

@userNotLogged
def profilUpdate(request):
    formProfil = profilForms(request.POST or None, request.FILES or None, instance=request.user.profil)
    formUser = userForms(request.POST or None, instance=request.user)
    dogum = Profil.objects.filter(user = request.user).first()
    keyword =request.POST.get("dogumGunu")
    if request.method == "POST":
        if formProfil.is_valid() and formUser.is_valid():
            formUser.save()
            profil = formProfil.save("commit=False")
            profil.dogum_gunu = keyword
            profil.save()
            messages.success(request, "Kayıt Edildi...")
        else:
            messages.warning(request,"Kayıt başarısız...")
        context={
            "formProfil":formProfil,
            "formUser":formUser,
            "dogumGunuu":dogum.dogum_gunu,
        }
        return redirect("kullaniciUpdate")
    context={
        "formProfil":formProfil,
        "formUser":formUser,
        "dogumGunuu":dogum.dogum_gunu,
    }
    return render(request, "User/updateProfil.html", context)


@userNotLogged
def resetPassword(request):
    form = resetPasswordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            kullanici = get_object_or_404(User, id = request.user.id)
            password = form.cleaned_data.get("password")
            kullanici.set_password(password)
            kullanici.save()
            messages.success(request, "Başarı ile değiştirildi..")
        else:
            messages.warning(request, "İşlem başarısız..")
        return redirect("kullaniciUpdate")
    context={
        "form":form,
    }
    return render(request, "User/giris.html", context)


def soruyorumUser(request, id, yazi):
    kullanici = get_object_or_404(User, id=id)
    kullaniciProfil =Profil.objects.get(user = kullanici)
    if yazi == "soru":
        sorular = Soru.objects.filter(reporter = id).order_by("-date")
        sorularSayi = Soru.objects.filter(reporter = id).count()
        context={
            "kullanici":kullanici,
            "sorular":sorular,
            "sorularSayi": sorularSayi,
            "kullaniciProfil": kullaniciProfil,
        }
        return render(request,"User/userSorular.html", context)
    elif yazi == "yorum":
        yorumlar = YorumSoru.objects.filter(reporter = id).order_by("-date")
        yorumlarSayi = YorumSoru.objects.filter(reporter = id).count()
        context={
            "kullanici":kullanici,
            "yorumlar": yorumlar,
            "kullaniciProfil": kullaniciProfil,
            "yorumlarSayi":yorumlarSayi,
        }
        return render(request,"User/userSorular.html", context)
    else:
        messages.warning(request, "Aradığınız istek bulunamadı..")
        return redirect("kullaniciDetail", id)

@userNotLogged
def profilUser(request):
    return render(request, "User/profil.html")


@userNotLogged
def begeniUser(request):
    sorular = BegenSoru.objects.filter(reporter=request.user)
    context={
        "sorular":sorular,
    }
    return render(request, "User/begeniler.html", context)




