from django.shortcuts import render,HttpResponse

# Create your views here.
def clubdash(request):
    return render(request,"clubdash.html")

def Dash(request):
    return render(request,"Dash.html")

def eventdash(request):
    return render(request,"eventdash.html")

def messagedash(request):
    return render(request,"messagedash.html")