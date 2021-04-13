from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static
from .views import RegistroPageView,ResetPageView,RegistrarPageView,HomePageView,DeportesPageView,NacionalesPageView,InternacionalesPageView,CoronavirusPageView,NoticePageView,AboutPageView

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
]