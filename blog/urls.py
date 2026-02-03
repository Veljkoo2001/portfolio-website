from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_list_view, name='blog'),
]