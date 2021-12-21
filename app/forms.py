
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CustomUserCreationForm(UserCreationForm):
	
	class Meta:
		model=User
		fields=["username","first_name","last_name","email","password1","password2"]
		help_texts = {k:"" for k in fields}

class Formulario_alta_post(forms.ModelForm):
	class Meta:
		model= Altapost
		fields='__all__'

class Formulario_comentario(forms.ModelForm):
	class Meta:
		model= Comentario
		fields='__all__'

class Formulario_comentarios_obj(forms.ModelForm):
	class Meta:
		model= ComentariosObj
		fields='__all__'

