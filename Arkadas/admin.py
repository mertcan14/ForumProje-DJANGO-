from django.contrib import admin
from .models import Arkadasım
# Register your models here.

class ArkadasimPage(admin.ModelAdmin):
    list_display=(
        'arkadas1',
        'arkadas2',
        'date',
    )
    list_filter = ('date',)

admin.site.register(Arkadasım, ArkadasimPage)
