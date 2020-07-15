from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.proyecto.models import Proyecto
from apps.proyecto.forms import ProyectoForm

def index_proyecto(request):
	return render(request, 'proyecto/index.html')


class ProyectoList(ListView):
	model = Proyecto
	template_name = 'Proyecto/index.html'


class ProyectoCreate(CreateView):
	model = Proyecto
	form_class = ProyectoForm
	template_name = 'proyecto/ingreso.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')


class ProyectoUpdate(UpdateView):
	model = Proyecto
	form_class = ProyectoForm
	template_name = 'proyecto/ingreso.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')


class ProyectoDelete(DeleteView):
	model = Proyecto
	template_name = 'proyecto/eliminar.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')