from rest_framework import serializers
from apimarketplace.models import *

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoItem
        fields = '__all__'


class RegiaoEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegiaoEntrega
        fields = '__all__'


class RegiaoEntregaCidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegiaoEntregaCidade
        fields = '__all__'


class TransportadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportadora
        fields = '__all__'


class TaxaEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxaEntrega
        fields = '__all__'


class TaxaEntregaTransportadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxaEntregaTransportadora
        fields = '__all__'

