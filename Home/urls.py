from django.urls import path,include
from . import views

urlpatterns = [

    path("",views.Home,name="home"),
    path("encrypte-decrypte/",views.EncrypteDecrypte,name="encrypte_decrypte"),
    path("encrypte/",views.EncrypteMessage,name="encrypte_message"),
    path("decrypte/",views.DecrypteMessage,name="decrypte_message"),
    path("higher-lower/",views.HigherLower,name="higher-lower"),
    path("quizler/",views.Quizler,name="quizler"),
    path("converter/",views.Converter,name="converter"),

]
