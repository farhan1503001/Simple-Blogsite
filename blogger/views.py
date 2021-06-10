from django.views.generic.detail import DetailView
from blogger.models import Post
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
#Now we will not use function views but class based template views
class Postlist(ListView):
    model=Post
    template_name='home.html'
#Now we will see the details views
class Postdetail(DetailView):
    model=Post 
    template_name='details.html'
#Now we will add post
class Addpost(SuccessMessageMixin,CreateView):
    model=Post
    template_name='add_post.html'
    fields='__all__'
    success_message='Post Created Successfully!'