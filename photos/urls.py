from django.urls import path, re_path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('search', views.search_images_by_category, name="search_results")
]