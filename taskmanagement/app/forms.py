from django.forms import ModelForm
from .models import Task
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput,TextInput
from django import forms
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
       

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())
#update a user
    
class UpdateUserForm(forms.ModelForm):
    password=None
    class Meta:
        model = User
        fields=['username','email']



