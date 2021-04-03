from django.urls import path
from .views import RegistrarPageView,HomePageView,DeportesPageView,NacionalesPageView,InternacionalesPageView,CoronavirusPageView,NoticePageView,AboutPageView

urlpatterns = [
	path('',HomePageView.as_view(),name = 'home'),
	path('deportes',DeportesPageView.as_view(),name = 'deportes'),
	path('nacionales',NacionalesPageView.as_view(),name = 'nacionales'),
	path('internacionales',InternacionalesPageView.as_view(),name = 'internacionales'),
	path('content',CoronavirusPageView.as_view(),name = 'content'),
	path('notice',NoticePageView.as_view(), name = 'notice'),
	path('about',AboutPageView.as_view(), name = 'about'),
	path('registrar/', RegistrarPageView.as_view(), name='registrar'),
	path('registrar/', RegistrarPageView.as_view(), name='reset'),
]