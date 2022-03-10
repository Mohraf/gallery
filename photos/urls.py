from django.urls import path, re_path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('search_category', views.search_images_by_category, name="search_results"),
  path('filter_location', views.home, name="locations")
]