from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from pagesapp.models import Student

# Create your views here.

class HomePageView(ListView):
    model = Student
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'