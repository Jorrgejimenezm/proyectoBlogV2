from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.inicio.as_view(), name='inicio'),
    path('listado/',views.listadoArticulos.as_view(),name='listado'),
    path('crear/',views.crearArticulo.as_view(),name='crear'),
    path('borrar/<int:pk>',views.borrarArticulo.as_view(),name='borrar'),
    path('modificar/<int:pk>',views.modificarArticulo.as_view(),name='modificar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)