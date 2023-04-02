from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class RegisterFrom(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class HomeForm(forms.Form):
    email = forms.EmailField(label=False)

