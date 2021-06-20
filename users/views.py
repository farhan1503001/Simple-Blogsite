from django.contrib.auth.views import PasswordChangeView
from users.forms import EditProfileForm, RegistrationForm, change_password_form
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
class password_change_view(PasswordChangeView):
    form_class=change_password_form
    template_name='registration/password.html'
    success_url=reverse_lazy('home')

class user_register(generic.CreateView):
    form_class=RegistrationForm #Using Pre-defined User Registration form We will change
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

class profile_edit(generic.UpdateView):
    form_class=EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')
    #Setting the form with logged in user

    def get_object(self):
        return self.request.user

