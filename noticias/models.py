from django.db import models

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

class User (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	descripcion = models.TextField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)

	def __str__ (self):
		return self.nombre

	def get_success_url(self):
		return reverse('login')