from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tweet

class TweetForm(forms.ModelForm):
    body = forms.CharField(required=True, 
                           widget=forms.Textarea(
                               attrs={
                                   'placeholder': "What's happening?",
                                   'class':'form-control',
                                   'rows': '4',
                                   'style': 'resize:none',
                                   }), 
                            label="")

    class Meta:
        model = Tweet
        fields = ['body']