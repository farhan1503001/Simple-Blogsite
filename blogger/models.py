from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.TextField()

    def __str__(self):
        return self.title+'||'+str(self.name)
    def get_absolute_url(self):
        return reverse('details',args=(str(self.pk)))
