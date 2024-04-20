#vista basada en funcion
from typing import Any
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import render
from core.erp.models import Category, Product
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt

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

    #def get_queryset(self):
    #    return Category.objects.filter(name__startswith='L')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name': 'william'}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        #context['object_list'] = Product.objects.all()
        return context