from email import message
from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
  images = Image.get_all_images()
  context ={
    "images": images
  }
  return render(request, 'index.html', context)


def search_images_by_category(request):
  if 'image' in request.GET and request.GET['image']:
    search_term = request.GET.get("image")
    images = Image.search_images(search_term)
    message = f"{search_term}"

    context = {
      "images": images,
      "message": message
    }

    return render(request, 'search_results.html', context)

  else:
    message = "You haven't searched for any term"
    return render(request, 'search_results.html',{"message":message})

