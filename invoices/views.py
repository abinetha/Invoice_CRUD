# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        print(serializer.is_valid(raise_exception=True))
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class InvoiceRetrieveView(generics.RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
