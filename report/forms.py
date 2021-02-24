from django import forms
from .models import ReportSoru


class reportForms(forms.ModelForm):
    class Meta:
        model = ReportSoru
        fields = ["content",]