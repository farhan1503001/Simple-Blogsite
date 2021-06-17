from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Count
from django.urls import reverse
from datetime import time,date,datetime
# Create your models here.
#Addition of field category
class Category(models.Model):
    name=models.CharField(max_length=250,default='coding')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title=models.CharField(max_length=200)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.TextField()
    #likes=models.ManyToManyFied(User,related_name='blog_post')
    category=models.CharField(max_length=250,default='coding')
    likes=models.ManyToManyField(User,related_name='blog_likes') #Adding new like fields
    post_date=models.DateTimeField(auto_now_add=True)#Will automatically add date and time field

    def get_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title+'||'+str(self.name)
    def get_absolute_url(self):
        return reverse('details',args=(str(self.pk)))
