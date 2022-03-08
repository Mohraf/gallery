from unicodedata import category
from django.db import models

# Create your models here.
class Image(models.Model):
  name = models.CharField(max_length=30)
  description = models.CharField(max_length=200)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  location = models.ForeignKey('Location', on_delete=models.CASCADE)


class Category(models.Model):
  WILDLIFE = 'WL'
  SPORTS = 'SP'
  FOOD = 'FD'
  PETS = 'PT'

  category_choices = [
    (WILDLIFE, 'Wildlife'),
    (SPORTS, 'Sports'),
    (FOOD, 'Food'),
    (PETS, 'Pets'),
  ]

  name = models.CharField(
    max_length=2,
    choices=category_choices,
    default=WILDLIFE,
  )

class Location(models.Model):
  name = models.CharField(max_length=20)