from django.contrib import admin
from .models import Categoria, Produto, Pedido, ItemPedido

# O comando admin.site.register() torna o modelo visível e gerível no painel de administração.
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(ItemPedido)