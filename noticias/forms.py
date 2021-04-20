from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import coronavirus,deportes,nacionales,internacionales


class CustomUser (UserCreationForm):
	pass


class coronaForm (forms.ModelForm):
	
	class Meta:
		model = coronavirus
		fields = '__all__'

class deportesForm (forms.ModelForm):
	
	class Meta:
		model = deportes
		fields = '__all__'

class NacionalesForm (forms.ModelForm):
	
	class Meta:
		model = nacionales
		fields = '__all__'

class interForm (forms.ModelForm):
	
	class Meta:
		model = internacionales
		fields = '__all__'

class noticiaForm (forms.ModelForm):
	
	class Meta:
		model = internacionales
		fields = '__all__'

