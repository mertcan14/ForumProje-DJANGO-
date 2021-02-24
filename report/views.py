from django.shortcuts import render, redirect
from Forum.views import userNotLogged
from .forms import reportForms
from Forum.models import Soru
from django.contrib import messages



@userNotLogged
def reportSoru(request, slug):
    form = reportForms(request.POST)
    if request.method == "POST":
        if form.is_valid():
            new = form.save(commit=False)
            new.kullanici = request.user
            new.soru = Soru.objects.get(slug=slug)
            new.save()
            messages.success(request, "Başarı ile iletildi")
        else:
            messages.info(request, "Lütfen seçim yapınız")
    return redirect("detailSoru", slug)