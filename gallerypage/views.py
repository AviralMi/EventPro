from django.shortcuts import render,HttpResponse

# Create your views here.
def gallerypage(request):
    return render(request,"G.html")