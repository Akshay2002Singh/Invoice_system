from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('invoice_data', views.get_invoice_data,name='get_data'),
    path('all_user_details', views.all_user_details,name='all_details'),
    path('generate_bill/<int:id>', views.generate_invoice,name='all_details'),
]