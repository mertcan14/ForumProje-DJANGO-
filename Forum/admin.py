from django.contrib import admin
from .models import Soru
# Register your models here.

class SoruPage(admin.ModelAdmin):
    prepopulated_fields= {"slug": ("title",)}
    list_display = (
        'title',
        'slug',
        'date',
        'reporter',
        'catego',
    )
    list_filter = ('catego','date')
    
admin.site.register(Soru, SoruPage)