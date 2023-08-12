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
                                   'rows': '1',
                                   'style': 'resize:none; color: white; font-size: 20px;',
                                   }), 
                            label="")

    class Meta:
        model = Tweet
        fields = ['body']