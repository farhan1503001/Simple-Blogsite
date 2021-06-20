from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models.base import Model
from django.forms import fields

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))#Using bootstrap to make it look better
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    #Now adding in runtime
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    #For changing username and password field appearenc
    def __init__(self, *args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'

class EditProfileForm(UserChangeForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    is_active=forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff=forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_superuser=forms.CharField(widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password','is_staff','is_active','date_joined')

class change_password_form(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')