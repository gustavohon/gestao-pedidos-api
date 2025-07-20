# Dentro de pedidos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Rotas para Categorias
    path('categorias/', views.CategoriaListCreateView.as_view(), name='lista-cria-categoria'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='detalhe-categoria'),

    # Rotas para Produtos
    path('produtos/', views.ProdutoListCreateView.as_view(), name='lista-cria-produto'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='detalhe-produto'),

    # Rotas para Pedidos
    path('pedidos/', views.PedidoListCreateView.as_view(), name='lista-cria-pedido'),
    path('pedidos/<int:pk>/', views.PedidoDetailView.as_view(), name='detalhe-pedido'),
]