from django.shortcuts import render

# Create your views here.
def number(request):
    d={'a':20,'b':40,'c':30,}
    return render(request,'number.html',d)