from rest_framework import serializers
from apimarketplace.models import *

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = '__all__'

