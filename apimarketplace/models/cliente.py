from django.db import models
from django.contrib.auth.models import User
from apimarketplace.models import Loja

class Cliente(models.Model):
    STATUS =(
        ('ATIVO','ATIVO'),
        ('INATIVO','INATIVO')
    )

    id_cliente = models.AutoField(primary_key=True)
    django_auth_user_id = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    id_loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=13)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    complemento = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS, default='ATIVO', max_length=10)
    email = models.EmailField(null=True)
    senha = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.nome

