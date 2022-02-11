from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', blank=True)
    def __str__(self):
        return self.title

class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(blank=True)
    message= models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
