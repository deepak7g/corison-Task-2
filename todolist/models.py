from django.db import models

# Create your models here.

class Task1(models.Model):
    name = models.CharField(max_length=100)
    descreption = models.CharField(max_length=100)
    datetime = models.CharField(max_length=100)
    time= models.CharField(max_length=100)


    def __str__(self):
        return self.name
