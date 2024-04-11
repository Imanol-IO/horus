from django.urls import path

from core.erp.views.category.views import category_list

app_name = 'erp'

urlpatterns = [
    path('category/list', category_list, name='category_list'),
   # path('uno/', myfistview, name='vista1'),
   # path('dos/', mysecondview, name='vista2')
]