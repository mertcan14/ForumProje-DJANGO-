from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.text import slugify 
Category={
    ('other','Diğer'),
    ('sport','Spor'),
    ('economy','Ekonomi'),
    ('health','Sağlık'),
    ('education','Eğitim'),
}


class Soru(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    catego = models.CharField(
        max_length=15,
        choices=Category,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Soru, self).save(*args, **kwargs)


class BegenSoru(models.Model):
    date =  models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    soru = models.ForeignKey(Soru, on_delete=models.CASCADE)
    repSor = models.CharField(max_length=200, unique=True)

class YorumSoru(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    soru = models.ForeignKey(Soru, on_delete=models.CASCADE)
    commit = models.CharField(max_length=300)
