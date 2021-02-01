from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dogum_gunu = models.DateField(
        verbose_name="Doğum Günü",
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Lokasyon",
    )
    hakkimda = models.TextField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="Hakkınızda"
    )
    user_image = models.ImageField(
        blank=True,
        null = True,
        verbose_name="Fotoğrafınız",
    )
    def __str__(self):
        return self.user
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profil.save()