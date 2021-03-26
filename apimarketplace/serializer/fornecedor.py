from rest_framework import serializers
from apimarketplace.models import *

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

