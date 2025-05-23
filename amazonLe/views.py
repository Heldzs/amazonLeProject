# from django.shortcuts import render
from rest_framework import viewsets, permissions
from amazonLe.models import Cliente, Pedido, Livro, Pedido_Livro
from amazonLe.serializers import (
    ClienteSerializer,
    PedidoSerializer,
    LivroSerializer,
    PedidoLivroSerializer,
)
from amazonLe.filters import FiltroCliente
from django_filters.rest_framework import DjangoFilterBackend


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FiltroCliente
    

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [permissions.IsAuthenticated]


class PedidoLivroViewSet(viewsets.ModelViewSet):
    queryset = Pedido_Livro.objects.all()
    serializer_class = PedidoLivroSerializer
    permission_classes = [permissions.IsAuthenticated]
