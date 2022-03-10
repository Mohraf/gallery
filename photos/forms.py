from random import choices
from django import forms
from .models import Location

locations = [location for location in Location.objects.all()]
length = len(locations)
ids = list(range(1, length+1))
choices = list(zip(ids, locations))


class ImageLocationFilterForm(forms.Form):
  location = forms.ChoiceField(widget=forms.Select, choices=choices)
