from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from djrichtextfield.models import RichTextField


STATUS = ((0, "Draft"), (1, "Published"))

class Holidays(models.Model):
    """
    A model to create and manage recipes
    """

    user = models.ForeignKey(
        User, related_name="holidays_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    slug = models.SlugField(max_length=200,null = True,)
    description = models.TextField(max_length=1000, null=False, blank=False)
    Recommendations = RichTextField(max_length=10000, null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


class Comment(models.Model):
    """This is the model for comments"""
    holidays = models.ForeignKey(
        Holidays, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    info = models.TextField()
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ["-date_added"]

def __str__(self):
    return str(self.title)