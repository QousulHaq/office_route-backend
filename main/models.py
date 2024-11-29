from django.db import models
from django.contrib.auth.models import User

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

class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # Create __str__ method to override the default one
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username