from django.db import models
from school.models import School, Classroom

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
