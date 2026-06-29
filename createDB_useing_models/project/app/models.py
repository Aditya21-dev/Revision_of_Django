from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name