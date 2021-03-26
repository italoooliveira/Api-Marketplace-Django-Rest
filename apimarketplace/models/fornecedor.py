from django.db import models
from apimarketplace.models import Loja

class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    id_loja = models.ManyToManyField(Loja)
    nome_fornecedor = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_fornecedor

