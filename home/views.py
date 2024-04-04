from django.shortcuts import render

# Create your views here.

def home(request):
    #return render(request, 'base.html')
    return render(request, 'home/home.html')
