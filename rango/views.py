from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage':"I am sent from context"}

    return render(request, 'rango/index.html', context_dict)

def about(request):
    return render(request, 'rango/about.html')
