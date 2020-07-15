from django.urls import path
from django.conf.urls import url, include
from apps.ecorregion.views import index_ecorregion, EcorregionList, EcorregionCreate, EcorregionUpdate, EcorregionDelete

app_name = 'ecorregion'

urlpatterns = [
	url(r'^index$',EcorregionList.as_view(), name="ecorregion_listar"),
	url(r'^nuevo$', EcorregionCreate.as_view(), name="ecorregion_nuevo"),
	url(r'^editar/(?P<pk>\d+)/$', EcorregionUpdate.as_view(), name="ecorregion_editar"),
	url(r'^eliminar/(?P<pk>\d+)/$',EcorregionDelete.as_view(), name="ecorregion_eliminar"),
]