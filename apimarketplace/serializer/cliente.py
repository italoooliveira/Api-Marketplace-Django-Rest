from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from apimarketplace.models import *
from django.contrib.auth.models import User, UserManager


class ClienteSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['nome'], email=validated_data['email']
        )
        user.set_password(validated_data['senha'])
        user.save()

        cliente = Cliente.objects.create(
            nome=user.username,
            django_auth_user_id=user,
            telefone=validated_data['telefone'],
            cep=validated_data['cep'],
            cidade=validated_data['cidade'],
            bairro=validated_data['bairro'],
            endereco=validated_data['endereco'],
            numero=validated_data['numero'],
            complemento=validated_data['complemento']
        )

        return cliente


    class Meta:
        model = Cliente
        fields = [
            'nome', 'email', 'senha',
            'telefone', 'cep', 'cidade', 'bairro', 'endereco', 'numero', 'complemento'
        ]


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'], email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


    class Meta:
        model = User
        fields = ['username', 'email', 'password']

