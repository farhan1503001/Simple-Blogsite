from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from blogger.models import Post
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PostForm,EditForm
from django.urls import reverse_lazy
# Create your views here.
#Now we will not use function views but class based template views
class Postlist(ListView):
    model=Post
    template_name='home.html'
    ordering=['post_date'
    ]
#Now we will see the details views
class Postdetail(DetailView):
    model=Post 
    template_name='details.html'
#Now we will add post
class Addpost(SuccessMessageMixin,CreateView):
    model=Post
    template_name='add_post.html'
    #fields='__all__'
    #For stylizing forms we use form
    form_class=PostForm
    success_message='Post Created Successfully!'
#Now we will Edit the post
class PostEdit(SuccessMessageMixin,UpdateView):
    model=Post
    template_name='update.html'
    #fields=('title','post')
    form_class=EditForm
    success_message='Post Updated Successfully'
#Now we will delete the post:
class DeletePost(DeleteView):
    model=Post
    template_name='delete.html'
    success_url=reverse_lazy('home')