from django.shortcuts import render

def python(request):
    d={'easy':'python is simplest language'}
    return render(request,'python.html',d)



