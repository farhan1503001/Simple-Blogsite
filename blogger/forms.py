from django import forms
from django.forms import fields, widgets
from .models import Post,Category

lister=Category.objects.all().values_list('name','name')
choice=[]
for item in lister:
    choice.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','name','category','post')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control','id':'name','value':'','type':'hidden'}),
            'category':forms.Select(choices=choice,attrs={'class':'form-control'}),
            'post': forms.Textarea(attrs={'class':'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','category','post')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice,attrs={'class':'form-control'}),
            'post': forms.Textarea(attrs={'class':'form-control'})
        }
class AddCateogory(forms.ModelForm):
    class Meta:
        model=Category
        fields=('name',)

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'})
        }