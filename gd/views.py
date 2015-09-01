from django.shortcuts import render

__author__ = 'naresh'
def home(request):
    return render(request, 'index.html')