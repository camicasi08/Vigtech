from django.conf.urls import patterns, include, url
from .views import *
from django.conf import settings

urlpatterns=patterns('',
	url(r'^$' ,login_required(home.as_view()), name='index'),
	url(r'^home/$' ,login_required(home.as_view()), name='home'),
	url(r'^gestionusuarios/registrar/$', RegistrarUsuario.as_view(), name='registrar_usuario'),
# url(r'^home/$' ,'buscador.views.indexarArchivos', name='indexar'),



)