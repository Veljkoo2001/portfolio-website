# projects/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list_view, name='projects'),
    #path('<int:project_id>/', views.project_detail_view, name='project_detail'),
]