from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import time,date,datetime
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.TextField()
    likes=models.ManyToManyField(User,related_name='blog_post')
    post_date=models.DateTimeField(auto_now_add=True)#Will automatically add date and time field

    def __str__(self):
        return self.title+'||'+str(self.name)
    def get_absolute_url(self):
        return reverse('details',args=(str(self.pk)))
