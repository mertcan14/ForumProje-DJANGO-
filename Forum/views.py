from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import kayitsoruForm, yorumsoruForm
from .models import Soru, BegenSoru, YorumSoru
from django.db.models.expressions import Func, Value
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from Arkadas.models import Arkadasım
from django.db.models import Q

def userNotLogged(func):
    def _func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)      
        messages.info(request,"Giriş Yapmanız Gerekiyor...")
        return redirect("kullaniciGiris")
    return _func
    

def anaSayfa(request, id=0):
    keyword = request.GET.get("SearchString")
    if request.user.is_authenticated:
        if id==0:
            if keyword is None:
                paylasimlar = Soru.objects.filter()
                paylasimlarr = Soru.objects.all().count()
                if paylasimlarr == 0:
                    return render(request, "Home/AnaSayfa.html")
                paylasimGundem = Soru.objects.order_by('?')[:5]
                liste = list()
                for paylasim in paylasimlar:
                    kontrol = str(paylasim.id) + str(request.user.id)
                    begenen = BegenSoru.objects.filter(repSor = kontrol).count()
                    if begenen != 0:
                        liste.append("True")
                    else:
                        liste.append("False")
            else:
                paylasimlar = Soru.objects.filter(title__icontains = keyword)
                paylasimlarr = Soru.objects.filter(title__icontains = keyword).count()
                if paylasimlarr == 0:
                    return render(request, "Home/AnaSayfa.html")
                paylasimGundem = Soru.objects.order_by('?')[:5]
                liste = list()
                for paylasim in paylasimlar:
                    kontrol = str(paylasim.id) + str(request.user.id)
                    begenen = BegenSoru.objects.filter(repSor = kontrol).count()
                    if begenen != 0:
                        liste.append("True")
                    else:
                        liste.append("False")
            paylasimlarZip = zip(paylasimlar, liste)
            context={
                "paylasimlar":paylasimlarZip,
                "paylasimGundem":paylasimGundem,
            }
            return render(request, "Home/AnaSayfa.html", context)
        else:
            liste = list()
            if keyword is None:
                if id == 1:
                    paylasimlar = Soru.objects.filter(catego = "sport").all()
                    paylasimlarr = Soru.objects.filter(catego = "sport").count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "sport").order_by('?')[:5]
                    
                elif id == 2:
                    paylasimlar = Soru.objects.filter(catego = "economy").all()
                    paylasimlarr = Soru.objects.filter(catego = "economy").count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "economy").order_by('?')[:5]

                elif id == 3:
                    paylasimlar = Soru.objects.filter(catego = "health").all()
                    paylasimlarr = Soru.objects.filter(catego = "health").count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "health").order_by('?')[:5]

                elif id == 4:
                    paylasimlar = Soru.objects.filter(catego = "education").all()
                    paylasimlarr = Soru.objects.filter(catego = "education").count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "education").order_by('?')[:5]

                elif id == 5:
                    paylasimlar = Soru.objects.filter(catego = "other").all()
                    paylasimlarr = Soru.objects.filter(catego = "other").count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "other").order_by('?')[:5]

                else:
                    return HttpResponseNotFound()
            else:
                if id == 1:
                    paylasimlar = Soru.objects.filter(catego = "sport").filter(title__icontains = keyword)
                    paylasimlarr = Soru.objects.filter(catego = "sport").filter(title__icontains = keyword).count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "sport").order_by('?')[:5]
                    
                elif id == 2:
                    paylasimlar = Soru.objects.filter(catego = "economy").filter(title__icontains = keyword)
                    paylasimlarr = Soru.objects.filter(catego = "economy").filter(title__icontains = keyword).count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "economy").order_by('?')[:5]

                elif id == 3:
                    paylasimlar = Soru.objects.filter(catego = "health").filter(title__icontains = keyword)
                    paylasimlarr = Soru.objects.filter(catego = "health").filter(title__icontains = keyword).count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "health").order_by('?')[:5]

                elif id == 4:
                    paylasimlar = Soru.objects.filter(catego = "education").filter(title__icontains = keyword)
                    paylasimlarr = Soru.objects.filter(catego = "education").filter(title__icontains = keyword).count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "education").order_by('?')[:5]

                elif id == 5:
                    paylasimlar = Soru.objects.filter(catego = "other").filter(title__icontains = keyword)
                    paylasimlarr = Soru.objects.filter(catego = "other").filter(title__icontains = keyword).count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "other").order_by('?')[:5]

                else:
                    return HttpResponseNotFound()

            for paylasim in paylasimlar:
                kontrol = str(paylasim.id) + str(request.user.id)
                begenen = BegenSoru.objects.filter(repSor = kontrol).count()
                if begenen != 0:
                    liste.append("True")
                else:
                    liste.append("False")
            paylasimlarZip = zip(paylasimlar, liste)
            context={
                "paylasimlar": paylasimlarZip,
                "paylasimGundem":paylasimGundem,
            }
            return render(request, "Home/AnaSayfa.html", context)
    else:
        if keyword is not None:
            if id==0:
                paylasimlar = Soru.objects.filter(title__icontains = keyword)
                paylasimlarr = Soru.objects.filter(title__icontains = keyword).count()
                if paylasimlarr == 0:
                    return render(request, "Home/AnaSayfa.html")
                paylasimGundem = Soru.objects.order_by('?')[:5]
                context={
                    "paylasimlarNot":paylasimlar,
                    "paylasimGundem":paylasimGundem,
                }
                return render(request, "Home/AnaSayfa.html", context)
            else:
                if id == 1:
                    paylasimlar = Soru.objects.filter(catego = "sport").filter(title__icontains = keyword)
                    paylasimlarr = Soru.objects.filter(catego = "sport").filter(title__icontains = keyword).count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "sport").order_by('?')[:5]
                elif id == 2:
                    paylasimlar = Soru.objects.filter(catego = "economy").filter(title__icontains = keyword)
                    paylasimlarr = Soru.objects.filter(catego = "economy").filter(title__icontains = keyword).count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "economy").order_by('?')[:5]
                elif id == 3:
                    paylasimlar = Soru.objects.filter(catego = "health").filter(title__icontains = keyword)
                    paylasimlarr = Soru.objects.filter(catego = "health").filter(title__icontains = keyword).count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "health").order_by('?')[:5]
                elif id == 4:
                    paylasimlar = Soru.objects.filter(catego = "education").filter(title__icontains = keyword)
                    paylasimlarr = Soru.objects.filter(catego = "education").filter(title__icontains = keyword).count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "education").order_by('?')[:5]
                elif id == 5:
                    paylasimlar = Soru.objects.filter(catego = "other").filter(title__icontains = keyword)
                    paylasimlarr = Soru.objects.filter(catego = "other").filter(title__icontains = keyword).count()
                    if paylasimlarr == 0:
                        return render(request, "Home/AnaSayfa.html")
                    paylasimGundem = Soru.objects.filter(catego = "other").order_by('?')[:5]
                else:
                    return HttpResponseNotFound()
        else:
            if id==0:
                paylasimlar = Soru.objects.all()
                paylasimGundem = Soru.objects.order_by('?')[:5]
                context={
                    "paylasimlarNot":paylasimlar,
                    "paylasimGundem":paylasimGundem,
                }
                return render(request, "Home/AnaSayfa.html", context)
            else:
                if id == 1:
                    paylasimlar = Soru.objects.filter(catego = "sport").all()
                    paylasimGundem = Soru.objects.filter(catego = "sport").order_by('?')[:5]
                elif id == 2:
                    paylasimlar = Soru.objects.filter(catego = "economy").all()
                    paylasimGundem = Soru.objects.filter(catego = "economy").order_by('?')[:5]
                elif id == 3:
                    paylasimlar = Soru.objects.filter(catego = "health").all()
                    paylasimGundem = Soru.objects.filter(catego = "health").order_by('?')[:5]
                elif id == 4:
                    paylasimlar = Soru.objects.filter(catego = "education").all()
                    paylasimGundem = Soru.objects.filter(catego = "education").order_by('?')[:5]
                elif id == 5:
                    paylasimlar = Soru.objects.filter(catego = "other").all()
                    paylasimGundem = Soru.objects.filter(catego = "other").order_by('?')[:5]
                else:
                    return HttpResponseNotFound()
        context={
            "paylasimlarNot": paylasimlar,
            "paylasimGundem":paylasimGundem,
        }
        return render(request, "Home/AnaSayfa.html", context)


@userNotLogged
def kayitSoru(request):
    form = kayitsoruForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            new = form.save(commit=False)
            new.reporter = request.user
            new.save()
            messages.success(request, "Başarı ile eklendi..")
            return redirect("AnaSayfa")
        else: 
            messages.info(request, "Maalesef eklenemedi..")
            context={
                "form":form,
            }
            return render(request,"Forum/kayitSoru.html", context)
    else:      
        context={
            "form":form,
        }
        return render(request,"Forum/kayitSoru.html", context)


def detail(request, slugg):
    paylasim = Soru.objects.get(slug = slugg)
    form = yorumsoruForm(request.POST or None)
    yorumlar = YorumSoru.objects.filter(soru = paylasim)
    next_issue = Soru.objects.filter(date__gt=paylasim.date).order_by('date').first()
    prev_issue = Soru.objects.filter(date__lt=paylasim.date).order_by('-date').first()
    """try:
        if request.META.get('HTTP_REFERER') == "http://127.0.0.1:8000/kategori/1":
            next_issue = Soru.objects.filter(date__gt=paylasim.date, catego="sport").order_by('date').first()
            prev_issue = Soru.objects.filter(date__lt=paylasim.date, catego="sport").order_by('-date').first()
        elif request.META.get('HTTP_REFERER') == "http://127.0.0.1:8000/kategori/2":
            next_issue = Soru.objects.filter(date__gt=paylasim.date, catego="economy").order_by('date').first()
            prev_issue = Soru.objects.filter(date__lt=paylasim.date, catego="economy").order_by('-date').first()
        elif request.META.get('HTTP_REFERER') == "http://127.0.0.1:8000/kategori/3":
            next_issue = Soru.objects.filter(date__gt=paylasim.date, catego="health").order_by('date').first()
            prev_issue = Soru.objects.filter(date__lt=paylasim.date, catego="health").order_by('-date').first()
        elif request.META.get('HTTP_REFERER') == "http://127.0.0.1:8000/kategori/4":
            next_issue = Soru.objects.filter(date__gt=paylasim.date, catego="education").order_by('date').first()
            prev_issue = Soru.objects.filter(date__lt=paylasim.date, catego="education").order_by('-date').first()
        elif request.META.get('HTTP_REFERER') == "http://127.0.0.1:8000/kategori/5":
            next_issue = Soru.objects.filter(date__gt=paylasim.date, catego="other").order_by('date').first()
            prev_issue = Soru.objects.filter(date__lt=paylasim.date, catego="other").order_by('-date').first()
        else:
            next_issue = Soru.objects.filter(date__gt=paylasim.date).order_by('date').first()
            prev_issue = Soru.objects.filter(date__lt=paylasim.date).order_by('-date').first()
    except:
        messages.info(request, "hata")"""
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                new = form.save(commit=False)
                new.reporter = request.user
                new.soru = paylasim
                new.save()
                messages.success(request,"Başarı ile gönderildi..")
            else: 
                messages.info(request, "Maalesef eklenemedi..")
        kontrol = str(paylasim.id) + str(request.user.id)
        begenen = BegenSoru.objects.filter(repSor = kontrol).count()
        context={
            "paylasim":paylasim,
            "form": form,
            "yorumlar": yorumlar,
            "begenen": begenen,
            "next_issue": next_issue,
            "prev_issue": prev_issue,
        }
        return render(request,"Forum/detail.html", context)
    else:
        begenen = 0
        context={
            "paylasim":paylasim,
            "form": form,
            "begenen": begenen,
            "yorumlar": yorumlar,
            "next_issue": next_issue,
            "prev_issue": prev_issue,
        }
        return render(request,"Forum/detail.html", context)

@userNotLogged
def arkadaslariminSorulari(request):
    arkadaslarim1 = Arkadasım.objects.filter(arkadas2 = request.user).values('arkadas1')
    arkadaslarim2 = Arkadasım.objects.filter(arkadas1 = request.user).values('arkadas2')
    paylasimlar = Soru.objects.filter(Q(reporter__in=arkadaslarim1) | Q(reporter__in=arkadaslarim2))
    paylasimGundem = Soru.objects.order_by('?')[:5]
    liste = list()
    for paylasim in paylasimlar:
        kontrol = str(paylasim.id) + str(request.user.id)
        begenen = BegenSoru.objects.filter(repSor = kontrol).count()
        if begenen != 0:
            liste.append("True")
        else:
            liste.append("False")
    paylasimlarZip = zip(paylasimlar, liste)
    context={
        "paylasimlar":paylasimlarZip,
        "paylasimGundem":paylasimGundem,
    }
    return render(request, "Home/AnaSayfa.html", context)


@userNotLogged
def SoruBegen(request, slugg):
    try:
        paylasim = get_object_or_404(Soru, slug = slugg)
        deger = str(paylasim.id) + str(request.user.id)
        newBegen = BegenSoru(reporter= request.user, soru= paylasim, repSor= deger)
        newBegen.save()
    except:
        messages.info(request,"Daha önceden beğenmişsiniz..")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@userNotLogged
def SoruBegenSil(request, slugg):
    try:
        paylasim = get_object_or_404(Soru, slug = slugg)
        deger = str(paylasim.id) + str(request.user.id)
        kontrol = BegenSoru.objects.get(repSor = deger)
        kontrol.delete()
    except:
        messages.WARNING(request, "Hata alındı..")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@userNotLogged
def yorumlarUser(request):
    yorumlar = YorumSoru.objects.filter(reporter=request.user)
    context={
        "yorumlar":yorumlar,
    }
    return render(request, "Forum/yorumlarUser.html", context)

@userNotLogged
def yorumSil(request, id):
    try:
        yorum = YorumSoru.objects.get(reporter = request.user, id = id)
        if yorum is None:
            messages.warning(request, "Maalesef yorum bulunamadı..")
            return redirect("kullaniciProfil")
        yorum.delete()
        return redirect("yorumlarUser")
    except:
        messages.warning(request, "Maalesef silmeye yetkiniz yok..")
        return redirect("kullaniciProfil")

@userNotLogged
def yorumUpdate(request, id):
    try:
        yorum = YorumSoru.objects.get(reporter=request.user, id=id)
        if yorum is None:
            messages.warning(request,"Maalesef yorum bulunamadı..")
            return redirect("yorumlarUser")
        form = yorumsoruForm(request.POST or None, instance=yorum)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request,"Başarı ile güncellendi..")
                return redirect("yorumlarUser")
            else:
                return redirect("yorumUpdateSoru", id)
        context={
            "form":form,
            "yorum":yorum,
        }
        return render(request, "Forum/yorumUpdate.html", context)
    except:
        messages.warning(request, "Maalesef erişme yetkiniz yok..")
        return redirect("kullaniciProfil")

@userNotLogged
def sorularUser(request):
    sorular = Soru.objects.filter(reporter=request.user)
    context ={
        "sorular": sorular,
    }
    return render(request,"Forum/sorularUser.html", context)

@userNotLogged
def soruUpdate(request, slugg):
    soru = Soru.objects.get(reporter=request.user, slug=slugg)
    form = kayitsoruForm(request.POST or None, instance=soru)
    if request.method =="POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Başarı ile güncellendi")
            return redirect("sorularUser")
        else:
            messages.warning(request, "Maalesef güncellenemedi")
    context={
        "form":form,
    }
    return render(request, "Forum/kayitSoru.html", context)

@userNotLogged
def soruSil(request, slugg):
    try:
        soru = Soru.objects.get(reporter=request.user, slug=slugg)
        if soru is None:
            messages.warning(request, "Maalesef Soru Bulunamadı")
            return redirect("sorularUser")
        soru.delete()
        messages.success(request, "Başarı ile silindi..")
        return redirect("sorularUser")
    except:
        messages.error(request, "Bu işlem için yetkiniz yok")
        return redirect("sorularUser")


