from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/',views.AboutView.as_view(), name='about'),
    path('craft/',views.CraftView.as_view(), name='craft'),
    path('products/',views.ProductsView.as_view(), name='products'),
    path('sustainability/',views.SustainabilityView.as_view(), name='sustainability'),
    path('contact/',views.ContactView.as_view(), name='contact'),
]