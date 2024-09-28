from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news_home'),
    path('create_news/', views.news_add, name='news_add'),


]