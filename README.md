#API de Gestão de Pedidos para Restaurantes

##📜 Sobre o Projeto
Este projeto é uma API RESTful completa para a gestão de um restaurante, desenvolvida com Django e Django REST Framework. Ele serve como o backend (o "cérebro") para qualquer aplicação cliente, como um site de pedidos, um aplicativo mobile ou um painel de controle interno.

##✨ Funcionalidades Principais
Gestão de Cardápio: Operações CRUD (Criar, Ler, Atualizar, Apagar) completas para Produtos e Categorias.

Gestão de Pedidos: Criação e visualização de Pedidos, incluindo os itens e suas quantidades.

API Navegável: Interface interativa e auto-documentada para testar os endpoints diretamente pelo navegador.

Painel de Administração: Interface de administração robusta e pronta para uso, fornecida pelo Django Admin, para gerenciamento de dados.

Endpoints da API
A URL base para todos os endpoints é /api/.

| Método | Endpoint | Descrição |
| GET, POST | /categorias/ | Lista todas as categorias ou cria uma nova. |
| GET, PUT, DELETE | /categorias/<id>/ | Visualiza, atualiza ou apaga uma categoria específica. |
| GET, POST | /produtos/ | Lista todos os produtos ou cria um novo. |
| GET, PUT, DELETE | /produtos/<id>/ | Visualiza, atualiza ou apaga um produto específico. |
| GET, POST | /pedidos/ | Lista todos os pedidos ou cria um novo. |
| GET, PUT, DELETE | /pedidos/<id>/ | Visualiza, atualiza ou apaga um pedido específico. |

##🚀 Como Rodar o Projeto Localmente
Siga os passos abaixo para configurar e executar o projeto no seu ambiente de desenvolvimento.

Pré-requisitos:

Python 3.x

Git

Passos:

Clone o repositório:

git clone https://github.com/gustavohon/gestao-pedidos-api.git
cd gestao-pedidos-api


Crie e ative o ambiente virtual:

# No Windows
python -m venv venv
.\venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Aplique as migrações do banco de dados:

python manage.py migrate


Crie um superusuário para acessar o painel de admin:

python manage.py createsuperuser
(irá pedir usuário, senha e e-mail)

Inicie o servidor de desenvolvimento:

python manage.py runserver
(CTRL+C fecha o servidor)

A API estará rodando em http://127.0.0.1:8000/api/. Você pode acessar o painel de administração em http://127.0.0.1:8000/admin/.