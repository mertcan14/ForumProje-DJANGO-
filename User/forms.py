from django import forms
from django.contrib.auth.models import User
from .models import Profil




class kayitForm(forms.Form):
    username=forms.CharField(
        label="Username",
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder':'username'})
    )
    email=forms.EmailField(
        label="E-Mail",
        max_length=254,
        widget=forms.TextInput(attrs={'placeholder':'e-mail'})
    )
    password=forms.CharField(
        label="Şifre",
        max_length=20,
        min_length=8,
        widget=forms.PasswordInput,
    )
    tekrar=forms.CharField(
        label="Şifre Tekrar",
        max_length=20,
        min_length=8,
        widget=forms.PasswordInput
    )

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        tekrar=self.cleaned_data.get("tekrar")
        email=self.cleaned_data.get("email")

        if password and tekrar and password!=tekrar:
            raise forms.ValidationError("Parola Uyuşmuyor..")

        values={
            "username":username,
            "password":password,
            "email":email
        }
        return values

class resetPasswordForm(forms.Form):
    password=forms.CharField(
        label="Şifre",
        max_length=20,
        min_length=8,
        widget=forms.PasswordInput,
    )
    tekrar=forms.CharField(
        label="Şifre Tekrar",
        max_length=20,
        min_length=8,
        widget=forms.PasswordInput
    )
    def clean(self):
        password=self.cleaned_data.get("password")
        tekrar=self.cleaned_data.get("tekrar")
        if password and tekrar and password!=tekrar:
            raise forms.ValidationError("Parola Uyuşmuyor..")
        values={
            "password":password,
        }
        return values
        


class girisForm(forms.Form):
    username=forms.CharField(
        label="Username",
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder':'User name'})
    )
    password=forms.CharField(
        label="Şifre",
        max_length=20,
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder':'Password'}),
    )




class profilForms(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ["location", "user_image", "hakkimda"]



class userForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


