from django.urls import path

from core.erp.views import myfistview, mysecondview

app_name = 'erp'

urlpatterns = [
    path('uno/', myfistview, name='vista1'),
    path('dos/', mysecondview, name='vista2')
]