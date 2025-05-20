from codecs import lookup
import django_filters
from amazonLe.models import Cliente, Pedido, Livro, Pedido_Livro

class FiltroCliente(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Cliente
        fields = ['nome', 'email']
