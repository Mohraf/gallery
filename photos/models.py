from unicodedata import category
from django.db import models

# Create your models here.
class Image(models.Model):
  name = models.CharField(max_length=30)
  description = models.CharField(max_length=200)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  location = models.ForeignKey('Location', on_delete=models.CASCADE)
  url_to_image = models.ImageField(upload_to="images/", default="image.png")

  def __str__(self):
    return self.name
  

  def save_image(self):
    self.save()


  def delete_image(self):
    self.delete()


  def update_image(self):
    self.update()

  
  @classmethod
  def get_all_images(cls):
    images = cls.objects.all()
    return images


  @classmethod
  def get_image_by_id(cls, id):
    image = cls.objects.get(id=id)
    return image
  

  @classmethod
  def search_images(cls, search_term):
    images = cls.objects.filter(category=search_term)
    return images
  

  @classmethod
  def filter_by_location(cls, location):
    images = cls.objects.filter(location=location)
    return images



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


  def __str__(self):
    return self.name


  def save_category(self):
    self.save()
  

  def delete_category(self):
    self.delete()
  

  def update_category(self):
    self.update()


class Location(models.Model):
  name = models.CharField(max_length=20)


  def __str__(self):
    return self.name
  

  def save_location(self):
    self.save()

  
  def delete_location(self):
    self.delete()
  

  def update_location(self):
    self.update()
