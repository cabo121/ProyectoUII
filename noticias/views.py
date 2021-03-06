from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import deportes,nacionales,internacionales,coronavirus
from .forms import noticiaForm,CustomUser, coronaForm, deportesForm, NacionalesForm, interForm
from django.contrib.auth.decorators import login_required, permission_required

class HomePageView(ListView):
	model = coronavirus
	template_name = 'home.html'
	context_object_name = 'noticias_list'

class DeportesPageView(ListView):
	model = deportes
	template_name = 'deportes.html'
	context_object_name = 'noticias_list'

class NacionalesPageView(ListView):
	model = nacionales
	template_name = 'nacionales.html'
	context_object_name = 'noticias_list'

class InternacionalesPageView(ListView):
	model = internacionales
	template_name = 'internacionales.html'
	context_object_name = 'noticias_list'

class CoronavirusPageView(ListView):
	model = coronavirus
	template_name = 'content.html'
	context_object_name = 'noticias_list'

class AboutPageView(ListView):
	model = coronavirus
	template_name = 'about.html'

class NoticePageView(ListView):
	model = coronavirus
	template_name = 'notice.html'
	context_object_name = 'noticias_list'

class RegistrarPageView (CreateView):
	model = User
	template_name = 'registrar.html'
	form_class =  UserCreationForm
	success_url = reverse_lazy('registro_success')

class RegistroPageView(ListView):
	model = coronavirus
	template_name = 'registro_success.html'

class ResetPageView (CreateView):
	model = User
	form_class =  UserCreationForm
	template_name = 'registration/reset.html'
	success_url = reverse_lazy('home')

def registro_usuario (request):
	data = {
		'form': CustomUser()
	}
	return render(request, 'registrar.html', data)	



# FUNCIONES QUE AGREGAN DATOS A LOS MODELOS

@permission_required('noticias.add_coronavirus')
def agregarCorona (request):
	data = {
		'form':coronaForm()
	}

	if request.method == 'POST':
		formulario = coronaForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
		else:
			data['form'] = formulario

	return render(request, 'agregarNoticia.html',data)

@permission_required('noticias.add_deportes')
def agregarDeportes (request):
	data = {
		'form':deportesForm()
	}

	if request.method == 'POST':
		formulario = deportesForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
		else:
			data['form'] = formulario

	return render(request, 'agregarNoticia.html',data)

@permission_required('noticias.add_nacionales')
def agregarNacionales (request):
	data = {
		'form':NacionalesForm()
	}

	if request.method == 'POST':
		formulario = NacionalesForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
		else:
			data['form'] = formulario

	return render(request, 'agregarNoticia.html',data)

@permission_required('noticias.add_internacionales')
def agregarInter (request):
	data = {
		'form':interForm()
	}

	if request.method == 'POST':
		formulario = interForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
		else:
			data['form'] = formulario

	return render(request, 'agregarNoticia.html',data)

# FUNCION QUE MUESTRA LAS CATEGORIAS 

def categoriasNoticias (request):

	return render(request, 'categoriasNoticias.html')


# FUNCIONES QUE MODIFICAN Y ELIMINAN DATOS

@permission_required('noticias.change_deportes')
def modificarNoticia (request, id):

	noticia = get_object_or_404(deportes, id=id)

	data = {
		'form': noticiaForm(instance=noticia)
	}

	if request.method == 'POST':
		formulario = noticiaForm(data=request.POST, instance=noticia)
		if formulario.is_valid():
			formulario.save()
			return redirect(to='deportes')
		data['form'] = formulario

	return render (request, 'modificar.html', data)

@permission_required('noticias.delete_deportes')
def eliminarNoticia (request, id):
	noticia = get_object_or_404(deportes, id=id)
	noticia.delete()

	return redirect(to = "deportes")


@permission_required('noticias.change_coronavirus')
def modificarNoticiaCoro (request, id):

	noticia = get_object_or_404(coronavirus, id=id)

	data = {
		'form': noticiaForm(instance=noticia)
	}

	if request.method == 'POST':
		formulario = noticiaForm(data=request.POST, instance=noticia)
		if formulario.is_valid():
			formulario.save()
			return redirect(to='content')
		data['form'] = formulario

	return render (request, 'modificar.html', data)

@permission_required('noticias.delete_coronavirus')
def eliminarNoticiaCoro (request, id):
	noticia = get_object_or_404(coronavirus, id=id)
	noticia.delete()

	return redirect(to = "content")

@permission_required('noticias.change_nacionales')
def modificarNoticiaNacio (request, id):

	noticia = get_object_or_404(nacionales, id=id)

	data = {
		'form': noticiaForm(instance=noticia)
	}

	if request.method == 'POST':
		formulario = noticiaForm(data=request.POST, instance=noticia)
		if formulario.is_valid():
			formulario.save()
			return redirect(to='nacionales')
		data['form'] = formulario

	return render (request, 'modificar.html', data)

@permission_required('noticias.delete_nacionales')
def eliminarNoticiaNacio (request, id):
	noticia = get_object_or_404(nacionales, id=id)
	noticia.delete()

	return redirect(to = "nacionales")


@permission_required('noticias.change_internacionales')
def modificarNoticiaInter (request, id):

	noticia = get_object_or_404(internacionales, id=id)

	data = {
		'form': noticiaForm(instance=noticia)
	}

	if request.method == 'POST':
		formulario = noticiaForm(data=request.POST, instance=noticia)
		if formulario.is_valid():
			formulario.save()
			return redirect(to='internacionales')
		data['form'] = formulario

	return render (request, 'modificar.html', data)

@permission_required('noticias.delete_internacionales')
def eliminarNoticiaInter (request, id):
	noticia = get_object_or_404(internacionales, id=id)
	noticia.delete()

	return redirect(to = "internacionales")