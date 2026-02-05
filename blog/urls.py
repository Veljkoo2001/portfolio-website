from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.blog_list, name='blog'),
    path('<slug:slug>/', views.blog_detail, name='blog_post_detail'),  # detalji posta
]