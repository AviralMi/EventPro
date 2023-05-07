from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("clubpage",views.clubpage,name="clubpage"),
]
