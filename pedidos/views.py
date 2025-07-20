from rest_framework import generics, status
from rest_framework.response import Response
from .models import Categoria, Produto, Pedido, ItemPedido
from .serializers import CategoriaSerializer, ProdutoSerializer, PedidoSerializer

# As "Generic Views" do Django REST Framework (DRF) fornecem um conjunto
# de blocos de construção para lidar com os padrões comuns de uma API.

# --- Views para Categoria ---

class CategoriaListCreateView(generics.ListCreateAPIView):
    """
    View para listar todas as categorias (GET) ou criar uma nova categoria (POST).
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para ver os detalhes (GET), atualizar (PUT/PATCH) ou apagar (DELETE)
    uma categoria específica.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# --- Views para Produto ---

class ProdutoListCreateView(generics.ListCreateAPIView):
    """
    View para listar todos os produtos (GET) ou criar um novo produto (POST).
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para ver os detalhes (GET), atualizar (PUT/PATCH) ou apagar (DELETE)
    um produto específico.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


# --- Views para Pedido ---

class PedidoListCreateView(generics.ListCreateAPIView):
    """
    View para listar todos os pedidos (GET) ou criar um novo pedido (POST).
    A lógica de criação (POST) será mais complexa, pois envolve criar
    também os Itens do Pedido. Por enquanto, vamos focar na listagem.
    """
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View para ver os detalhes (GET), atualizar o status (PUT/PATCH) ou 
    cancelar (DELETE) um pedido específico.
    """
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer