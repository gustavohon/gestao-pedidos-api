from rest_framework import serializers
from .models import Categoria, Produto, Pedido, ItemPedido

# Um Serializer converte dados complexos, como os nossos modelos Django,
# num formato que pode ser facilmente renderizado em JSON.
# Também faz o processo inverso: converte dados JSON recebidos numa requisição
# de volta para objetos Django que podem ser guardados na base de dados.

class CategoriaSerializer(serializers.ModelSerializer):
    # A classe Meta diz ao serializer qual modelo ele deve usar e quais campos
    # desse modelo devem ser incluídos na "tradução".
    class Meta:
        model = Categoria
        # '__all__' é um atalho para incluir todos os campos do modelo.
        # Neste caso, incluirá 'id' e 'nome'.
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    # Para tornar a nossa API mais informativa, em vez de mostrarmos apenas o ID da categoria,
    # podemos mostrar o nome da categoria.
    # O 'source' aponta para o campo 'nome' do modelo Categoria relacionado.
    # 'read_only=True' significa que este campo é apenas para leitura; não o usaremos para criar/atualizar produtos.
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)

    class Meta:
        model = Produto
        # Incluímos todos os campos do modelo Produto e o nosso campo personalizado 'categoria_nome'.
        fields = ['id', 'nome', 'descricao', 'preco', 'categoria', 'categoria_nome']
        # O campo 'categoria' será usado para escrever (criar/atualizar), enquanto 'categoria_nome' será para ler.
        extra_kwargs = {'categoria': {'write_only': True}}


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        # Vamos expor apenas os campos relevantes para um item dentro de um pedido.
        fields = ['produto', 'quantidade']


class PedidoSerializer(serializers.ModelSerializer):
    # Quando virmos um pedido, não queremos ver apenas os IDs dos itens,
    # queremos ver os detalhes. Usamos o ItemPedidoSerializer para isso.
    # 'many=True' indica que um pedido pode ter múltiplos itens.
    itens = ItemPedidoSerializer(many=True, read_only=True, source='itempedido_set')

    class Meta:
        model = Pedido
        # Definimos os campos que a nossa API de Pedidos irá mostrar.
        fields = ['id', 'mesa', 'status', 'criado_em', 'itens']