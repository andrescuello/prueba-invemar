from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.ecorregion.models import Ecorregion
from apps.ecorregion.forms import EcorregionForm

def index_ecorregion(request):
	return render(request, 'ecorregion/index.html')


class EcorregionList(ListView):
	model = Ecorregion
	template_name = 'ecorregion/index.html'


class EcorregionCreate(CreateView):
	model = Ecorregion
	form_class = EcorregionForm
	template_name = 'Ecorregion/ingreso.html'
	success_url = reverse_lazy('ecorregion:ecorregion_listar')


class EcorregionUpdate(UpdateView):
	model = Ecorregion
	form_class = EcorregionForm
	template_name = 'ecorregion/ingreso.html'
	success_url = reverse_lazy('ecorregion:ecorregion_listar')


class EcorregionDelete(DeleteView):
	model = Ecorregion
	template_name = 'ecorregion/eliminar.html'
	success_url = reverse_lazy('ecorregion:ecorregion_listar')