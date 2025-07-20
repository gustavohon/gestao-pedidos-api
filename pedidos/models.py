from django.db import models

# Modelo para as categorias dos produtos (ex: Bebidas, Lanches, Sobremesas)
# Esta classe irá criar uma tabela 'Categoria' no banco de dados.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, help_text="Nome único para a categoria")

    # Esta função especial define como o objeto será exibido no painel de admin do Django.
    # Em vez de mostrar "Categoria object (1)", mostrará o nome real, como "Bebidas".
    def __str__(self):
        return self.nome

# Modelo para os produtos do cardápio
# Esta classe irá criar uma tabela 'Produto' no banco de dados.
class Produto(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do produto")
    descricao = models.TextField(blank=True, help_text="Descrição opcional do produto")
    preco = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço do produto")
    
    # ForeignKey cria uma relação "um-para-muitos". 
    # Um produto pertence a UMA categoria, mas uma categoria pode ter VÁRIOS produtos.
    # on_delete=models.CASCADE significa que, se uma categoria for apagada, todos os produtos nela também serão.
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

# Modelo para os pedidos feitos pelos clientes
# Esta classe irá criar uma tabela 'Pedido' no banco de dados.
class Pedido(models.Model):
    # Opções pré-definidas para o status do pedido, para evitar erros de digitação.
    STATUS_CHOICES = [
        ('recebido', 'Recebido'),
        ('em_preparo', 'Em Preparo'),
        ('pronto', 'Pronto'),
        ('entregue', 'Entregue'),
    ]
    mesa = models.IntegerField(help_text="Número da mesa que fez o pedido")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='recebido')
    
    # ManyToManyField cria uma relação "muitos-para-muitos". 
    # Um pedido pode ter VÁRIOS produtos, e um produto pode estar em VÁRIOS pedidos.
    # Usamos 'through' para especificar um modelo intermediário (ItemPedido) onde guardaremos
    # informações extras sobre essa relação, como a quantidade de cada item.
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    criado_em = models.DateTimeField(auto_now_add=True) # Guarda a data e hora exatas da criação do pedido.

    def __str__(self):
        return f"Pedido da Mesa {self.mesa} - {self.status}"

# Modelo intermediário para armazenar a quantidade de cada produto em um pedido
# Esta é a nossa tabela de junção personalizada para a relação muitos-para-muitos.
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1, help_text="Quantidade do produto no pedido")

    # A classe Meta permite-nos adicionar configurações extras ao nosso modelo.
    class Meta:
        # Garante que um mesmo produto não possa ser adicionado duas vezes no mesmo pedido.
        # A combinação de 'pedido' e 'produto' deve ser sempre única.
        unique_together = ('pedido', 'produto')