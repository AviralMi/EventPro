from django.shortcuts import render,HttpResponse

# Create your views here.

def Register(request):
    return render(request,"Register.html")

def login(request):
    return render(request,"login.html")

def forpim(request):
    return render(request,"forpim.html")

def forpvid(request):
    return render(request,"forpvid.html")