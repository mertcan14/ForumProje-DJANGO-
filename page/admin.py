from django.contrib import admin
from .models import Sayfa

class SayfaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'title',
        'slug',
        'date',
        'statu',
    )
    list_editable = ('statu',)

admin.site.register(Sayfa, SayfaAdmin)