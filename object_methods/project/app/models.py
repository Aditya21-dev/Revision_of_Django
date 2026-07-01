from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    marks = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    admission_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name