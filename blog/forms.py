from django import forms
from .models import BlogPost
from django import forms
from django.contrib.auth.forms import UserCreationForm


class PostForm(UserCreationForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'img_url', 'category', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

            'img_url': forms.TextInput(attrs={'class': 'form-control'}),

            }


class FeaturedPostForm(UserCreationForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'img_url', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'img_url': forms.TextInput(attrs={'class': 'form-control'}),

            }
