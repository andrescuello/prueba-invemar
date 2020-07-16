from django.urls import path
from django.conf.urls import url, include
from apps.proyecto.views import index_proyecto, ProyectoList, ProyectoCreate, ProyectoUpdate, ProyectoDelete, ReporteProyectoExcel


app_name = 'proyecto'

urlpatterns = [
	url(r'^index$',ProyectoList.as_view(), name="proyecto_listar"),
	url(r'^nuevo$', ProyectoCreate.as_view(), name="proyecto_nuevo"),
	url(r'^proyectoexcel$', ReporteProyectoExcel.as_view(), name="proyecto_excel"),
	url(r'^editar/(?P<pk>\d+)/$', ProyectoUpdate.as_view(), name="proyecto_editar"),
	url(r'^eliminar/(?P<pk>\d+)/$',ProyectoDelete.as_view(), name="proyecto_eliminar"),
]

	