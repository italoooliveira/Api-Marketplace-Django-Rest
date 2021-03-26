from rest_framework import serializers
from apimarketplace.models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class ProdutoImagemSerializer(serializers.ModelSerializer):
    imagem = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = ProdutoImagem
        fields = '__all__'


class ProdutoAtributoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoAtributo
        fields = '__all__'


class ProdutoAtributoValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoAtributoValor
        fields = '__all__'


class ProdutoComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoComentario
        fields = '__all__'