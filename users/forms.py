from django.contrib.auth.forms import UserCreationForm
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