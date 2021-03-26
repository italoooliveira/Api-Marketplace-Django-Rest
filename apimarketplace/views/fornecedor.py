from rest_framework import viewsets
from apimarketplace.models import *
from apimarketplace.serializer import *

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

