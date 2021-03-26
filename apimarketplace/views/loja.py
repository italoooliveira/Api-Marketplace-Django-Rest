from rest_framework import viewsets
from apimarketplace.models import *
from apimarketplace.serializer.loja import *


class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer