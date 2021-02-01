from django.db import models
from django.contrib.auth.models import User

class ArkadasIstek(models.Model):
    atanKullanici = models.ForeignKey(User, on_delete=models.CASCADE, related_name="atanKullanici")
    alanKullanici = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alanKullanici")
    atal = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


class Arkadasım(models.Model):
    arkadas1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="arkadas1")
    arkadas2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="arkadas2")
    arkadas1_2=models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
