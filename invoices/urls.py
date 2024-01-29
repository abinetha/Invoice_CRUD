# urls.py
from django.urls import path
from .views import InvoiceListCreateView, InvoiceRetrieveView

urlpatterns = [
    path('invoice/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoice/<int:pk>/', InvoiceRetrieveView.as_view(), name='invoice-retrieve'),
]
