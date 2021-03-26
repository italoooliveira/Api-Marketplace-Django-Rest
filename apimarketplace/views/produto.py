from rest_framework import viewsets
from apimarketplace.models import *
from apimarketplace.serializer import *

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoImagemViewSet(viewsets.ModelViewSet):
    queryset = ProdutoImagem.objects.all()
    serializer_class = ProdutoImagemSerializer


class ProdutoAtributoViewSet(viewsets.ModelViewSet):
    queryset = ProdutoAtributo.objects.all()
    serializer_class = ProdutoAtributoSerializer


class ProdutoAtributoValorViewSet(viewsets.ModelViewSet):
    queryset = ProdutoAtributoValor.objects.all()
    serializer_class = ProdutoAtributoValorSerializer


class ProdutoComentarioViewSet(viewsets.ModelViewSet):
    queryset = ProdutoComentario.objects.all()
    serializer_class = ProdutoComentarioSerializer

