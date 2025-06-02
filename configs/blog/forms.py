from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',
                  'content',
                  'price',
                  'photo',
                  'video',
                  'category')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Content',
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price',
            }),
            'video': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Video',
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=16, help_text='Maximum 16 characters',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username'
                               }))

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Password'
                               }))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
