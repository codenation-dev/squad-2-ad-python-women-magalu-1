# Projeto Final - Python Woman (Magalu)

Para rodar o projeto:

### Ambiente Virtual

1- Instalar o ambiente virtual:
> pip3 install virtualenv

2 - Criar o ambiente virtual:
> virtualenv venv -p python3

3 - Ativar o ambiente virtual:
> source venv/bin/activate 

4 - Instalar as dependências:
> pip3 install -r requirements.txt

### Migrations

Acessar do projeto: errorcenter

1 - Criar as migrations
> pip3 manage.py migrate

2 - Criar super usuário
> pip3 manage.py createsuperuser

### Iniciar

1 - Rodar o servidor
> pip3 manage.py runserver