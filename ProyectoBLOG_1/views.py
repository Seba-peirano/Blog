from django.views.generic import TemplateView
from django.shortcuts import render

def HomePageView(request):
    return render(request, "blog/index.html") 

