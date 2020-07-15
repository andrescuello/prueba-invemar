from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.registro.models import Registro
from apps.registro.forms import RegistroForm

def index_registro(request):
	return render(request, 'registro/index.html')


class RegistroList(ListView):
	model = Registro
	template_name = 'registro/index.html'


class RegistroCreate(CreateView):
	model = Registro
	form_class = RegistroForm
	template_name = 'registro/ingreso.html'
	success_url = reverse_lazy('registro:registro_listar')


class RegistroUpdate(UpdateView):
	model = Registro
	form_class = RegistroForm
	template_name = 'registro/ingreso.html'
	success_url = reverse_lazy('registro:registro_listar')


class RegistroDelete(DeleteView):
	model = Registro
	template_name = 'registro/eliminar.html'
	success_url = reverse_lazy('registro:registro_listar')
