from django import forms
from apps.proyecto.models import Proyecto
from django.conf import settings


class ProyectoForm(forms.ModelForm):

	class Meta:
		model = Proyecto

		fields = [
			'nombre',
            'informacion',   
		]
		labels = {
			'nombre': 'Nombre',
            'informacion': 'Información',
		}
		widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'informacion': forms.Textarea(attrs={'class':'form-control'}),
		}