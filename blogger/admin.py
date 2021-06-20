from blogger.models import Post
from django.contrib import admin
from . models import Category, Post, comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(comment)