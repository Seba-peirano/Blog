from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from .models import Post

class RegistroUsuarioForm(UserCreationForm):
    #estoy cambiando el usercreationform por uno propio
    username=forms.CharField(label="Ingrese Nombre")
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class PostFormulario(forms.ModelForm):
    
    class Meta:
        model=Post
        fields='__all__'

