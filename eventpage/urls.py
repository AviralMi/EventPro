from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("eventpage",views.eventpage,name="eventpage"),
]
