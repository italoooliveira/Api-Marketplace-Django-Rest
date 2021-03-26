from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from apimarketplace.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cliente', ClienteViewSet, basename='Clientes')
router.register('fornecedor', FornecedorViewSet, basename='Fornecedores')
router.register('pedido', PedidoViewSet, basename='Pedidos')
router.register('pedido_item', PedidoItemViewSet, basename='PedidoItem')
router.register('regiao-entrega', RegiaoEntregaViewSet, basename='RegiaoEntrega')
router.register('transportadora', TransportadoraViewSet, basename='Transportadora')
router.register('taxa-entrega', TaxaEntregaViewSet, basename='TaxaEntrega')
router.register('taxa-entrega-transportadora', TaxaEntregaTransportadoraViewSet, basename='TaxaEntregaTransportadora')
router.register('categoria', CategoriaViewSet, basename='Categorias')
router.register('produto', ProdutoViewSet, basename='Produtos')
router.register('produto_imagem', ProdutoImagemViewSet, basename='ProdutoImagem')
router.register('produto_atributo', ProdutoAtributoViewSet, basename='ProdutoAtributo')
router.register('produto_atributo_valor', ProdutoAtributoValorViewSet, basename='ProdutoAtributoValor')
router.register('produto_comentario', ProdutoComentarioViewSet, basename='ProdutoComentario')
router.register('usuario', UserViewSet, basename='Usuario')
router.register('loja', LojaViewSet, basename='Loja')

urlpatterns = router.urls

