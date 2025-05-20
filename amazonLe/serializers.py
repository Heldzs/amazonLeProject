from rest_framework import serializers
from amazonLe.models import Cliente, Pedido, Livro, Pedido_Livro


class ClienteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)

    class Meta:
        model = Cliente
        fields = "__all__"


class PedidoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    cliente = ClienteSerializer()
    data_pedido = serializers.DateField()

    class Meta:
        model = Pedido
        fields = "__all__"


class LivroSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Livro
        fields = "__all__"


class PedidoLivroSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    cliente = ClienteSerializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(), source="cliente", write_only=True
    )
    pedido = PedidoSerializer(read_only=True)
    pedido_id = serializers.PrimaryKeyRelatedField(
        queryset=Pedido.objects.all(), source="pedido", write_only=True
    )
    livro = LivroSerializer(read_only=True)
    livro_id = serializers.PrimaryKeyRelatedField(
        queryset=Livro.objects.all(), source="livro", write_only=True
    )

    class Meta:
        model = Pedido_Livro
        fields = "__all__"
