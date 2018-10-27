from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ngo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=5000)
    website = models.URLField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.PositiveIntegerField()


class ReliefCamp(models.Model):
    title = models.CharField(max_length=200)
    lat = models.FloatField()
    long = models.FloatField()
    image = models.ImageField()


# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=None )

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    contact = models.PositiveIntegerField()


    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
