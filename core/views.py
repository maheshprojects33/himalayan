from logging import Filter

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
        context["our_craft"] = OurCraft.objects.last()
        context["faqs"] = Faq.objects.all().order_by('id')
        return context

class AboutView(ListView):
    model = AboutBanner
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_banner"] = AboutBanner.objects.last()
        context["our_story"] = OurStory.objects.last()
        context["message"] = MessageFromCEO.objects.last()
        context["our_values"] = OurValue.objects.all()
        context["capabilities"] = Capability.objects.last()
        
        return context
    

class CraftView(ListView):
    model = OurCraftBanner
    template_name = 'core/craft.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["banner"] = OurCraftBanner.objects.last()
        context["processes"] = OurCraftProcess.objects.all()
        context["points"] = OurCraftQuality.objects.all()
        context["images"] = GalleryInside.objects.all()

        return context

class ProductsView(ListView):
    model = AllProducts
    template_name = 'core/products.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["filter_tags"] = FilterTag.objects.all()
            context["products"] = AllProducts.objects.all()
            context["ordering"] = ProductOrdering.objects.all()

            
            return context

class SustainabilityView(ListView):
    model = SustainabilityBanner
    template_name = 'core/sustainability.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["banner"] = SustainabilityBanner.objects.last()
        context["community"] = SustainabilityCommunity.objects.last()
        context["practices"] = SustainabilityPractice.objects.all()
        context["commitment"] = SustainabilityCommitment.objects.last()

        return context

class ContactView(TemplateView):
    template_name = 'core/contact.html'