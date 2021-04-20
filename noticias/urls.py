from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static
from .views import modificarNoticiaNacio,eliminarNoticiaNacio,modificarNoticiaInter,eliminarNoticiaInter,modificarNoticiaCoro,eliminarNoticiaCoro,eliminarNoticia,modificarNoticia,agregarCorona,agregarDeportes,agregarNacionales,agregarInter,categoriasNoticias,RegistroPageView,ResetPageView,RegistrarPageView,HomePageView,DeportesPageView,NacionalesPageView,InternacionalesPageView,CoronavirusPageView,NoticePageView,AboutPageView

urlpatterns = [
	path('',HomePageView.as_view(),name = 'home'),
	path('deportes',DeportesPageView.as_view(),name = 'deportes'),
	path('nacionales',NacionalesPageView.as_view(),name = 'nacionales'),
	path('internacionales',InternacionalesPageView.as_view(),name = 'internacionales'),
	path('content',CoronavirusPageView.as_view(),name = 'content'),
	path('notice',NoticePageView.as_view(), name = 'notice'),
	path('about',AboutPageView.as_view(), name = 'about'),
	path('registro_success',RegistroPageView.as_view(), name = 'registro_success'),
	path('registrar/', RegistrarPageView.as_view(), name='registrar'),
	path('registrar/reset',auth_views.PasswordResetView.as_view(), name='reset'),
	path('agregarCorona/', agregarCorona, name = 'agregarCorona' ),
	path('agregarDeportes/', agregarDeportes, name = 'agregarDeportes' ),
	path('agregarNacionales/', agregarNacionales, name = 'agregarNacionales' ),
	path('agregarInter/', agregarInter, name = 'agregarInter' ),
	path('categoriasNoticias/', categoriasNoticias, name = 'categoriasNoticias'),
	path('modificarNoticia/<id>/', modificarNoticia, name = 'modificarNoticia'),
	path('eliminarNoticia/<id>/', eliminarNoticia, name = 'eliminarNoticia'),
	path('modificarNoticiaCoro/<id>/', modificarNoticiaCoro, name = 'modificarNoticiaCoro'),
	path('eliminarNoticiaCoro/<id>/', eliminarNoticiaCoro, name = 'eliminarNoticiaCoro'),
	path('modificarNoticiaNacio/<id>/', modificarNoticiaNacio, name = 'modificarNoticiaNacio'),
	path('eliminarNoticiaNacio/<id>/', eliminarNoticiaNacio, name = 'eliminarNoticiaNacio'),
	path('modificarNoticiaInter/<id>/', modificarNoticiaInter, name = 'modificarNoticiaInter'),
	path('eliminarNoticiaInter/<id>/', eliminarNoticiaInter, name = 'eliminarNoticiaInter'),
]