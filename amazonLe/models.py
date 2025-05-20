from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Cliente(ModelBase):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.id} - {self.nome}"


class Livro(ModelBase):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    ano_publicacao = models.IntegerField(null=True)
    quantidade_estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.titulo} - Qtd: {self.quantidade_estoque}"


class Pedido(ModelBase):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Pedido de {self.cliente.nome} para {self.livro.titulo}"


class Pedido_Livro(ModelBase):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return f"{self.quantidade}x {self.livro.titulo} em {self.pedido}"
