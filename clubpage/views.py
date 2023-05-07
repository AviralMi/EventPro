from django.shortcuts import render,HttpResponse

# Create your views here.
def clubpage(request):
    return render(request,"club.html")