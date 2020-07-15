from django import forms
from apps.ecorregion.models import Ecorregion
from django.conf import settings


class EcorregionForm(forms.ModelForm):

	class Meta:
		model = Ecorregion

		fields = [
			'nombre',  
		]
		labels = {
			'nombre': 'Nombre',
		}
		widgets = {
            'nombre':  forms.TextInput(attrs={'class':'form-control'}),
		}