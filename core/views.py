from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name='core/home.html'
    
class TestView(TemplateView):
    template_name='core/test.html'