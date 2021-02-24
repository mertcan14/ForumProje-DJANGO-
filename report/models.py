from django.db import models
from django.contrib.auth.models import User
from Forum.models import Soru

reportChocies ={
    ('spam','spam'),
    ('nudity','+18'),
    ('violence','Şiddet'),
    ('fraud','Sahtekarlık'),
}


class ReportSoru(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    soru = models.ForeignKey(Soru, on_delete= models.CASCADE)
    kullanSoru = models.CharField(max_length=100)
    content = models.CharField(choices=reportChocies, max_length=15)
    date = models.DateTimeField(auto_now_add=True)

