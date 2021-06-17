from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
class user_register(generic.CreateView):
    form_class=UserCreationForm #Using Pre-defined User Registration form We will change
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

