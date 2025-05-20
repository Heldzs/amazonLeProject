from django.urls import path, include
from rest_framework.routers import DefaultRouter
from amazonLe.views import ClienteViewSet, PedidoViewSet, LivroViewSet, PedidoLivroViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'livros', LivroViewSet)
router.register(r'pedido_livro', PedidoLivroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]