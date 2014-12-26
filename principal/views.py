from django.shortcuts import render, render_to_response, redirect, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.template import RequestContext
from .forms import *
import sys    # sys.setdefaultencoding is cancelled by site.py
reload(sys)    # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding('utf-8')
# Create your views here.
#@login_required
class home(TemplateView):
	template_name="home.html"

class RegistrarUsuario(FormView):
	template_name="registrarUsuario.html"
	form_class=FormularioRegistrarUsuario
	success_url = reverse_lazy('RegistrarUsuarios')

	def form_valid(self, form):
		user=form.save()
		messages.success(self.request, "Se ha creado exitosamente el usuario")
		return redirect('login')