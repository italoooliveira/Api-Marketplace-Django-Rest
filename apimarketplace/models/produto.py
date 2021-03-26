from django.db import models
from apimarketplace.models import Fornecedor, Cliente, Loja


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria_pai = models.ForeignKey("Categoria", on_delete=models.CASCADE, null=True, blank=True)
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_categoria


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome_produto = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    marca = models.CharField(max_length=100)
    id_categoria = models.ManyToManyField(Categoria)
    id_fornecedor = models.ManyToManyField(Fornecedor, null=True, blank=True)
    produto_pai = models.ForeignKey("Produto", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome_produto


class ProdutoImagem(models.Model):
    id_imagem = models.AutoField(primary_key=True)
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    imagem = models.ImageField(null=True, blank=True, upload_to="./imagens/")

    def __str__(self):
        return self.url


class ProdutoAtributo(models.Model):
    id_atributo = models.AutoField(primary_key=True)
    nome_atributo = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_atributo


class ProdutoAtributoValor(models.Model):
    id_atributo = models.ForeignKey(ProdutoAtributo, on_delete=models.CASCADE)
    valor = models.CharField(max_length=255)


class ProdutoComentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    comentario = models.TextField()

    def __str__(self):
        return self.comentario


class ProdutoCupom(models.Model):
    id_cupom = models.AutoField(primary_key=True)
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    desconto = models.FloatField()
    validade = models.FloatField(null=True)

