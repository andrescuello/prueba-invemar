from django.urls import path
from django.conf.urls import url, include
from apps.registro.views import index_registro, RegistroList, RegistroCreate, RegistroUpdate, RegistroDelete, RegistroDetail, ReporteRegistroExcel

app_name = 'registro'

urlpatterns = [
	url(r'^index$',RegistroList.as_view(), name="registro_listar"),
	url(r'^nuevo$', RegistroCreate.as_view(), name="registro_nuevo"),
	url(r'^reporte_excel$', ReporteRegistroExcel.as_view(), name="registro_excel"),
	url(r'^editar/(?P<pk>\d+)/$', RegistroUpdate.as_view(), name="registro_editar"),
	url(r'^eliminar/(?P<pk>\d+)/$',RegistroDelete.as_view(), name="registro_eliminar"),
	url(r'^detalle/(?P<pk>\d+)/$',RegistroDetail.as_view(), name="registro_detalle"),

]