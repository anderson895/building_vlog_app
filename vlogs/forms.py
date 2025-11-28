from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import VlogPost


class VlogPostForm(forms.ModelForm):
    class Meta:
        model = VlogPost
        fields = ['title', 'video_url', 'description', 'tags', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter vlog title'
        })
        self.fields['video_url'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Paste video URL (YouTube, Vimeo, etc.)'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Write a description for your vlog',
            'rows': 4
        })
        self.fields['tags'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add comma-separated tags'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-select'
        })


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email address'
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        }),
        help_text=""
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password'
        }),
        help_text=""
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registered.")
        return email

# ------------------------------
# User Login Form
# ------------------------------
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
