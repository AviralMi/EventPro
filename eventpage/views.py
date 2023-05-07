from django.shortcuts import render,HttpResponse

# Create your views here.
def eventpage(request):
    return render(request,"Events_hai.html")