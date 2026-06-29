from django.db import models

# Create your models here.

# ==========================
# Student Model
# ==========================

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # classroom = models.ForeignKey(Class , on_delete=models.CASCADE)
    Class_room = models.ForeignKey("Class" , on_delete=models.CASCADE)
    subjects = models.ManyToManyField("Subject")

    def __str__(self):
        return self.name
    

# ==========================
# Teacher Model
# ==========================

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.name


# ==========================
# Class Model
# ==========================

class Class(models.Model):
    class_name = models.CharField(max_length=50)
    room_no = models.IntegerField()

    def __str__(self):
        return self.class_name


# ==========================
# Subject Model
# ==========================

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    teacher = models.OneToOneField(Teacher , on_delete=models.CASCADE , related_name="subject")

    def __str__(self):
        return self.subject_name
    


# ==========================
# ID Card Model
# ==========================

class IDCard(models.Model):
    card_number = models.CharField(max_length=20)
    issue_date = models.DateField()
    student = models.OneToOneField(Student , on_delete=models.CASCADE  ,related_name="id_card")

    def __str__(self):
        return self.card_number