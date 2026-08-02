from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'core/homepage.html'

class AboutView(TemplateView):
    template_name = 'core/about.html'

class CraftView(TemplateView):
    template_name = 'core/craft.html'

class ProductsView(TemplateView):
    template_name = 'core/products.html'

class SustainabilityView(TemplateView):
    template_name = 'core/sustainability.html'

class ContactView(TemplateView):
    template_name = 'core/contact.html'