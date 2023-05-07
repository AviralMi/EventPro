from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("clubdash",views.clubdash,name="clubdash"),
    path("Dash",views.Dash,name="Dash"),
    path("eventdash",views.eventdash,name="eventdash"),
    path("messagedash",views.messagedash,name="messagedash"),
]
