from django.contrib import admin

from .models import deportes,nacionales,internacionales,coronavirus

modelos = deportes,nacionales,internacionales,coronavirus
admin.site.register(modelos)


