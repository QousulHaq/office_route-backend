from django.db import models

# Create your models here.

class Course(models.Model):
    image = models.ImageField(upload_to='courses/')
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.PositiveSmallIntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Service(models.Model):
    icon = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title