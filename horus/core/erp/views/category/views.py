#vista basada en funcion
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from core.erp.models import Category, Product
from django.views.generic import ListView

# vistas basadas en funciones
def category_list(request):
    data = {
        'title': 'Listado de Categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

# vistas basadas en clases
class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    def get_queryset(self):
        return Category.objects.filter(name__startswith='L')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        #context['object_list'] = Product.objects.all()
        return context