from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    refcode = models.CharField(max_length=10, default=None)
    catg = models.CharField(max_length=50, default=None)
    desc = models.TextField(max_length=300, null=True)
    teacher = models.CharField(max_length=100)
