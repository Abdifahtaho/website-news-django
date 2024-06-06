from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    created_by=models.IntegerField()

    def __str__(self):
        return self.name
    
class Post(models. Model):
    title= models.CharField(max_length=100)
    slug=models. SlugField(max_length=200)
    category=models. ForeignKey (category, on_delete=models.CASCADE)
    image=models. ImageField(upload_to='static/images')
    content=models.TextField()
    published=models.BooleanField (default=False)
    tags=models. CharField(max_length=20)
    created= models. DateTimeField(auto_now_add=True)
    created_by=models.IntegerField()
    def __str__(self):
        return self.title

class contact(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    phone=models.CharField(max_length=40)
    email=models.CharField(max_length=20)
    images=models. ImageField(upload_to='static/images')
    video = models.FileField(upload_to='static/videos', null=True, blank=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
