from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    profile_image = models.ImageField(null = True)
    followers = models.ManyToManyField("self", blank = True)
    following = models.ManyToManyField("self" , blank=True)
    website = models.CharField(max_length = 100 , null = True)
    intro = models.TextField(null = True)
    phone = models.CharField(max_length = 100 , null = True)
    
    @property
    def images_count(self):
        return self.images.all().count()

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()

