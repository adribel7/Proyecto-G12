from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
	nombre=models.CharField('Nombre de la Categoria',max_length=50,null=False,blank=False)
	descripcion=models.TextField()
	fecha_elaboracion=models.DateField()
	imagen=models.ImageField(upload_to="categorias",null=True)


	def __str__(self):
		return self.nombre

class Objetivo(models.Model):
	nombre=models.CharField('Nombre del Objetivo',max_length=50)
	descripcion=models.TextField()
	categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
	fecha_elaboracion=models.DateField()
	imagen=models.ImageField(upload_to="objetivos",null=True)

	def __str__(self):
		return self.nombre	


class Altapost(models.Model):
	titulo=models.CharField('Nombre del Titulo',max_length=50)
	imagen=models.ImageField(upload_to="altapost",null=True)
	descripcion=models.TextField()
	categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
	usuario=models.ForeignKey(User, on_delete=models.PROTECT)
	fecha_elaboracion=models.DateField(auto_now=True)

	def get_absolute_url(self):
    		
		return reverse('blog')

	def __str__(self):
		return self.titulo

class Comentario(models.Model):
	usuario=models.ForeignKey(User, on_delete=models.PROTECT)
	post=models.ForeignKey(Altapost, on_delete=models.CASCADE, related_name='comments')
	fecha_creacion=models.DateTimeField(auto_now=True)
	descripcion=models.TextField()
	
	def get_absolute_url(self):

		return reverse('blog')

	def __str__(self):
		return self.descripcion
	
class ComentariosObj(models.Model):
	usuario=models.ForeignKey(User, on_delete=models.PROTECT)
	post=models.ForeignKey(Objetivo, on_delete=models.CASCADE, related_name='comentarios')
	fecha_creacion=models.DateTimeField(auto_now=True)
	descripcion=models.TextField()

	def get_absolute_url(self):

		return reverse('blog')

	def __str__(self):
		return self.descripcion

