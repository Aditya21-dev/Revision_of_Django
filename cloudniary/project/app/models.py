from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Image(models.Model):
    image = CloudinaryField("image")

    def __str__(self):
        return f"Image {self.id}"
    

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    profile_img = CloudinaryField("profile image")

    def __str__(self):
        return self.name