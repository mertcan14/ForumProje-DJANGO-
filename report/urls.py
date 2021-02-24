from django.urls import path
from .views import reportSoru

urlpatterns = [
    path('reportSoru/<slug:slug>', reportSoru, name="reportSoru"),
]