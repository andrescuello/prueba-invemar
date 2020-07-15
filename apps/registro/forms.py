from django import forms
from apps.registro.models import Registro
from django.conf import settings


class RegistroForm(forms.ModelForm):

	class Meta:
		model = Registro

		fields = [
			'especie',
            'familia',
            'nombrecomun',
            'proyecto',
            'baseregistro',
            'identificador',
            'añoidentificacion',
            'departamento',
            'municipio',
            'localidad',
            'latitud',
            'longitud',
            'autor',
            'fechacaptura',
            'ecorregion',
		]
		labels = {
			'especie': 'Especie',
            'familia': 'Familia',
            'nombrecomun': 'Nombre comun',
            'proyecto': 'Proyecto',
            'baseregistro': 'Base del registro',
            'identificador': 'Identificador',
            'añoidentificacion': 'Año identificación',
            'departamento': 'Departamento',
            'municipio': 'Municipio',
            'localidad': 'Localidad',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'autor': 'Autor',
            'fechacaptura': 'Fecha de captura',
            'ecorregion': 'Ecorregión',
		}
		widgets = {
			'especie': forms.TextInput(attrs={'class':'form-control'}),
            'familia': forms.TextInput(attrs={'class':'form-control'}),
            'nombrecomun': forms.TextInput(attrs={'class':'form-control'}),
            'proyecto': forms.SelectMultiple(attrs={'class':'form-control', 'size':'10'}),
            'baseregistro': forms.TextInput(attrs={'class':'form-control'}),
            'identificador': forms.TextInput(attrs={'class':'form-control'}),
            'añoidentificacion': forms.TextInput(attrs={'class':'form-control'}),
            'departamento': forms.TextInput(attrs={'class':'form-control'}),
            'municipio': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'latitud': forms.TextInput(attrs={'class':'form-control'}),
            'longitud': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class':'form-control'}),
            'fechacaptura': forms.DateInput(attrs={'class':'form-control fecha-date'},format='%Y-%m-%d'),
            'ecorregion': forms.SelectMultiple(attrs={'class':'form-control', 'size':'10'}),
		}