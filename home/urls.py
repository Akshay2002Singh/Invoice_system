from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('invoice_data', views.get_invoice_data,name='get_data'),
]