from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
  return render(request, 'index.html')


def search_images_by_category(request, search_term):
  images = Image.search_images(search_term)

  context = {
    "images": images
  }

  return render(request, 'search_results.html', context)