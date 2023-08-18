from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'class':'form-control row mb-3', 'placeholder':'Username'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control row mb-3', 'type':'email','placeholder':'name@email.com'}))
    password1 = forms.CharField(label='Password', max_length=50, widget=forms.TextInput(attrs={'class':'form-control row mb-3', 'type':'password', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password', max_length=50, widget=forms.TextInput(attrs={'class':'form-control row mb-3', 'type':'password', 'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class EditProfileForm(forms.ModelForm):
    name = forms.CharField(label='Name',  max_length=10, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    profile_bio = forms.CharField(label='Profile Bio',  max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Profile Bio'}))
    class Meta:
        model = Profile
        fields =['name', 'profile_pic', 'profile_bio']
