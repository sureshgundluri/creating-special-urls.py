from django.shortcuts import render

def arundathi(request):
    d={'name':'sweety','movie':'arundathi'}
    return render(request,'arundathi.html',d)


def sonusood(request):
    d={'pasupathi':'vadala bomalli vadala'}
    return render(request,'sonusood.html',d)

def anuskha(request):
    d={'arundathi':'nuvu nannu amm cheyalevu ra'}
    return render(request,'anuskha.html',d)

def java(request):
    d={'hard':'as compared with python java is difficult'}
    return render(request,'java.html',d)
