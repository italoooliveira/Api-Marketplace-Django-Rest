from django.db import models


class Loja(models.Model):
    id_loja = models.AutoField(primary_key=True)
    nome_loja = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    cep = models.CharField(max_length=25)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    numero = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome_loja

