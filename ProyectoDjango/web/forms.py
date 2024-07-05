from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'gmail', 'contraseña']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['gmail', 'contraseña']