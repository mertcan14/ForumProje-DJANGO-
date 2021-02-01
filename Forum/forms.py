from django import forms
from .models import Soru, YorumSoru


class kayitsoruForm(forms.ModelForm):
    class Meta:
        model=Soru
        fields =  ["title", "content", "catego"]

class yorumsoruForm(forms.ModelForm):
    class Meta:
        model = YorumSoru
        fields = ["commit",]