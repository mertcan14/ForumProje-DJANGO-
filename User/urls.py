from django.urls import path, include
from User.views import kayitUser, cikisUser, girisUser,detailUser, profilUpdate, resetPassword, soruyorumUser, profilUser, begeniUser

urlpatterns = [
    path('giris/', girisUser, name="kullaniciGiris"),
    path('kayit/', kayitUser, name="kullaniciKayit"),
    path('cikis/', cikisUser, name="kullaniciCikis"),
    path('profil/', profilUser, name="kullaniciProfil"),
    path('profil/begeni/', begeniUser, name="kullaniciBegeni"),
    path('updateProfil/', profilUpdate, name="kullaniciUpdate"),
    path('detail/<int:id>', detailUser, name="kullaniciDetail"),
    path('detail/<int:id>/<str:yazi>', soruyorumUser, name="soruyorumUser"),
    path('resetPassword/', resetPassword, name="kullaniciResetpassword"),
]
