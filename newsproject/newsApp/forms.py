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


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','password']


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())