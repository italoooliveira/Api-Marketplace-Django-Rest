from rest_framework import viewsets
from apimarketplace.models import *
from apimarketplace.serializer import *

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PedidoItemViewSet(viewsets.ModelViewSet):
    queryset = PedidoItem.objects.all()
    serializer_class = PedidoItemSerializer


class RegiaoEntregaViewSet(viewsets.ModelViewSet):
    queryset = RegiaoEntrega.objects.all()
    serializer_class = RegiaoEntregaSerializer


class RegiaoEntregaCidadeViewSet(viewsets.ModelViewSet):
    queryset = RegiaoEntregaCidade.objects.all()
    serializer_class = RegiaoEntregaCidadeSerializer


class TransportadoraViewSet(viewsets.ModelViewSet):
    queryset = Transportadora.objects.all()
    serializer_class = TransportadoraSerializer


class TaxaEntregaViewSet(viewsets.ModelViewSet):
    queryset = TaxaEntrega.objects.all()
    serializer_class = TaxaEntregaSerializer


class TaxaEntregaTransportadoraViewSet(viewsets.ModelViewSet):
    queryset = TaxaEntregaTransportadora.objects.all()
    serializer_class = TaxaEntregaTransportadoraSerializer

