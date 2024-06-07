from django import forms
from .models import category, Post,contact
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name', 'created_by']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'category', 'image', 'content', 'published', 'tags', 'created_by']


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['fname', 'lname', 'phone', 'email', 'images', 'video']


