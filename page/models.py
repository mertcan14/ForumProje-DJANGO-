from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify 

Status={
    ('unprepared','Hazırlanmamış'),
    ('prepared','Hazır'),
    ('showing','Gösterimde')
}

class Sayfa(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content= RichTextField()
    statu=models.CharField(max_length=15, choices=Status)
    date=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Sayfa, self).save(*args, **kwargs)
