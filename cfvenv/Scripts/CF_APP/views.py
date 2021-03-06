from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'django/index.html')
    return render(request, 'django/page1.html')