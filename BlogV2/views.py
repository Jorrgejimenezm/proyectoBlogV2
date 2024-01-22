from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Articulo


# Create your views here.

class inicio (TemplateView):
    template_name='BlogV2/index.html'

class listadoArticulos(ListView):
    model = Articulo

class crearArticulo(CreateView):
    model = Articulo
    fields =['titulo','texto','imagen','categorias']
    success_url = reverse_lazy('listado')

    def form_valid(self, form): #validador de datos del usuario
        form.instance.autor = self.request.user #el usuario que esta identificado en el admin es el que crea el articulo por defecto
        return super(crearArticulo,self).form_valid(form)

class borrarArticulo(DeleteView):
    model = Articulo
    success_url = reverse_lazy('listado')

class modificarArticulo(UpdateView):
    model = Articulo
    fields = ['titulo','texto','imagen','categorias']
    template_name_suffix = "_update_form"
    success_url =reverse_lazy('listado')
