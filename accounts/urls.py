from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("Register",views.Register,name="Register"),
    path("login",views.login,name="login"),
    path("forpim",views.forpim,name="forpim"),
    path("forpvid",views.forpvid,name="forpvid"),
]
