
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return self.name

class Education(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    course = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.student.name}'s Education"
