from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import User,deportes,nacionales,internacionales,coronavirus

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
	Success_url = reverse_lazy('home')