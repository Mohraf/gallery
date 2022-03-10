from email import message
from email.mime import image
from multiprocessing import context
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
  images = Image.get_all_images()
  context ={
    "images": images
  }
  form = ImageLocationFilterForm()
  context["form"] = form

  if request.method == 'POST':
    form = ImageLocationFilterForm(request.POST)
    if form.is_valid():
      location = form.cleaned_data['location']
      images = Image.filter_by_location(location)
      context["images"] = images

  return render(request, 'index.html', context)


def search_images_by_category(request):
  context = {}
  form = ImageLocationFilterForm()
  context["form"] = form

  if request.method == 'POST':
    form = ImageLocationFilterForm(request.POST)
    if form.is_valid():
      location = form.cleaned_data['location']
      images = Image.filter_by_location(location)
      context["images"] = images

  
  if 'image' in request.GET and request.GET['image']:
    search_term = request.GET.get("image")
    images = Image.search_images(search_term)
    message = f"{search_term}"

    context["images"] = images
    context["message"] = message
    # context = {
    #   "images": images,
    #   "message": message
    # }

    return render(request, 'search_results.html', context)

  else:
    message = "You haven't searched for any term"
    return render(request, 'search_results.html',{"message":message})


def filter_images_by_location(request):
  if 'image' in request.GET and request.GET['image']:
    search_term = request.GET.get("image")
    images = Image.filter_by_location(search_term)
    message = f"{search_term}"

    context = {
      "images": images,
      "message": message
    }

    return render(request, 'search_results.html', context)

  else:
    message = "You haven't searched for any term"
    return render(request, 'search_results.html',{"message":message})
