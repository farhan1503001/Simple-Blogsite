from users.forms import RegistrationForm
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
class user_register(generic.CreateView):
    form_class=RegistrationForm #Using Pre-defined User Registration form We will change
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

class profile_edit(generic.UpdateView):
    form_class=UserChangeForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')
    #Setting the form with logged in user

    def get_object(self):
        return self.request.user

