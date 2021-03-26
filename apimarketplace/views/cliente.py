from rest_framework import viewsets
from apimarketplace.models import *
from apimarketplace.serializer import *
from django.contrib.auth.models import User


class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

