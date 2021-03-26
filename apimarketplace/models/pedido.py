from django.db import models
from datetime import datetime
from apimarketplace.models import Produto, Cliente, Loja

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    data = models.DateField(default=datetime.now())
    previsao_entrega = models.DateField(null=True, blank=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    tipo_pagamento = models.CharField(max_length=100)

    def __str__(self):
        return self.id_pedido


class PedidoItem(models.Model):
    id_pedido_item = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=13, decimal_places=2)


class RegiaoEntrega(models.Model):
    id_regiao = models.AutoField(primary_key=True)
    nome_regiao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_regiao


class RegiaoEntregaCidade(models.Model):
    id_cidade = models.AutoField(primary_key=True)
    id_regiao = models.ForeignKey(RegiaoEntrega, on_delete=models.CASCADE)
    nome_cidade = models.CharField(max_length=255, null=True)
    cep = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome_cidade


class Transportadora(models.Model):
    id_transportadora = models.AutoField(primary_key=True)
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome_transportadora = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_transportadora


class TaxaEntrega(models.Model):
    id_regiao = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)


class TaxaEntregaTransportadora(models.Model):
    id_regiao = models.ForeignKey(TaxaEntrega, on_delete=models.PROTECT)
    id_transportadora = models.ForeignKey(Transportadora, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=12, decimal_places=2)

