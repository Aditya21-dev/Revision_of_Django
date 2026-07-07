from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Image(models.Model):
    image = CloudinaryField("image")

    def __str__(self):
        return f"Image {self.id}"