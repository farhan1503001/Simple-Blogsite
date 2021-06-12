from django import forms
from django.forms import fields, widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','name','post')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control','id':'name','value':'','type':'hidden'}),
            'post': forms.Textarea(attrs={'class':'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','post')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'post': forms.Textarea(attrs={'class':'form-control'})
        }