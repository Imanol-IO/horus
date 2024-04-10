from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from core.erp.models import Category, Product

# Create your views here.

#vista basada en funcion
def myfistview(request):
    data = {
        'name': 'imanol',
        'categorias': Category.objects.all()
    }
    return render(request, 'home.html', data) 

def mysecondview(request):
    data = {
        'name': 'imanol',
        'categorias': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data) 