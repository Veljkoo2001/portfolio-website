from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path("projects/", include("projects.urls")),
]
