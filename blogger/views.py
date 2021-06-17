from django.http import request
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from blogger.models import Post
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Category, Post
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AddCateogory, PostForm,EditForm
from django.urls import reverse_lazy
# Create your views here.
#Now we will not use function views but class based template views
class Postlist(ListView):
    model=Post
    template_name='home.html'
    ordering=['-post_date']
    #For getting context value in homepage
    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(Postlist,self).get_context_data()
        context['cat_menu']=cat_menu
        return context
#Now we will see the details views
class Postdetail(DetailView):
    model=Post 
    template_name='details.html'
#Showing category details
def category_detail(request,cats):
    cat_data=Post.objects.filter(category=cats)
    return render(request,'category_detail.html',{'cats':cat_data})
#Now we will add post
class Addpost(SuccessMessageMixin,CreateView):
    model=Post
    template_name='add_post.html'
    #fields='__all__'
    #For stylizing forms we use form
    form_class=PostForm
    success_message='Post Created Successfully!'
#Here we will add new categories
class AddCategories(CreateView):
    model=Category
    template_name='add_category.html'
    form_class=AddCateogory
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
class UserPost(ListView):
    model=Post
    template_name='user_post.html'

    def get_queryset(self):
       query_set=Post.objects.filter(name=self.request.user)
       return query_set