#importing path from main urls
from django.urls import path
#importing views
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('author/<str:pk_id>/', views.authorPage, name='authorPage'),
    path('create/<str:author_id>/', views.createPage, name='create_blog'),
]
