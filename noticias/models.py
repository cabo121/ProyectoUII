from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractUser )

class deportes (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	descripcion = models.TextField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	autor = models.CharField(default = "",null=True,max_length = 200)
	
	def __str__ (self):
		return self.nombre

class nacionales (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	descripcion = models.TextField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	autor = models.CharField(default = "",null=True,max_length = 200)
	
	def __str__ (self):
		return self.nombre
		
class internacionales (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	descripcion = models.TextField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	autor = models.CharField(default = "",null=True,max_length = 200)
	
	def __str__ (self):
		return self.nombre

class coronavirus (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	descripcion = models.TextField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	autor = models.CharField(default = "",null=True,max_length = 200)
	
	def __str__ (self):
		return self.nombre


# class User(AbstractUser):
#     edad = models.PositiveIntegerField(null =True, blank = True)
#     telefono = models.PositiveIntegerField(null =True, blank = True)
#     genero = models.CharField(null =True, blank = True)
#     email = models.EmailField(null = True, blank = True)




