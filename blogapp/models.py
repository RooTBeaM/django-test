from distutils.command.upload import upload
import email
from pyexpat import model
from statistics import mode
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Blog(models.Model): 
    title = models.CharField(max_length=120) 
    post = models.TextField() 
    date_created = models.DateTimeField(auto_now_add=True) 
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    #link show image
    #need python -m pip install Pillow
    #need type python manage.py makemigrations
    #save to database by python manage.py migrate
    feild_img = models.ImageField(upload_to='featured_img', blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    subject = models.CharField(max_length=120)
    sender = models.CharField(max_length=80)
    email = models.EmailField()
    detail = models.TextField()

    def __str__(self):
        return self.subject