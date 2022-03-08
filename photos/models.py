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


  def update_image(self, update_details):
    self.update(update_details)


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