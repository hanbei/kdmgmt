from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    birth_date = models.DateTimeField()
    gender = models.CharField(max_length=1)
    grade = models.CharField(max_length=10)
    email = models.EmailField()
    club = models.CharField(max_length=100)
    zekken = models.BooleanField()
    jacket = models.BooleanField()
    joined = models.DateField()