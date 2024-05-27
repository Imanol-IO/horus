from django.urls import path

from core.erp.views.category.views import *
from core.erp.views.client.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
   # path('uno/', myfistview, name='vista1'),
   # path('dos/', mysecondview, name='vista2')
]