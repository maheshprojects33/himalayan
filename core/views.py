from django.views.generic import TemplateView, ListView
from core.models import *
# Create your views here.
class HomeView(ListView):
    model = HeroImageSlider
    template_name = 'core/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hero_images"] = HeroImageSlider.objects.all()
        context["who_we_are"] = WhoWeAre.objects.last()
        context["what_we_make"] = WhatWeMake.objects.all()
        return context

class AboutView(ListView):
    model = AboutBanner
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_banner"] = AboutBanner.objects.last()
        context["message"] = MessageFromCEO.objects.last()
        return context
    

class CraftView(TemplateView):
    template_name = 'core/craft.html'

class ProductsView(TemplateView):
    template_name = 'core/products.html'

class SustainabilityView(TemplateView):
    template_name = 'core/sustainability.html'

class ContactView(TemplateView):
    template_name = 'core/contact.html'