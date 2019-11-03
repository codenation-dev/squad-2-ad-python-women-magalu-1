# Projeto Final - Central de Erros
# Aceleração Python Woman (Luiza Labs) 
# Squad 2

Para executar o projeto:

### Clonar repositório

Clonar o repositório no seu computador:
    $ cd pasta-desejada
    $ git clone https://github.com/codenation-dev/squad-2-ad-python-women-magalu-1.git

### Virtualenv

1- Instalar o Virtualenv:
> pip3 install virtualenv

### Ambiente virtual

1 - Criar o ambiente virtual com Virtualenv:
> cd squad-2-ad-python-women-magalu-1
> virtualenv venv -p python3

2 - Ativar o ambiente virtual:
> source venv/bin/activate 

3 - Instalar as dependências:
> pip3 install -r requirements.txt

### Migrations

1 - Criar as migrations
> cd errorcenter
> pip3 manage.py makemigrations
> pip3 manage.py migrate

2 - Criar super usuário
> pip3 manage.py createsuperuser

### Tela de Login

1 - Executar o servidor
> pip3 manage.py runserver

2 - Acessar a url inicial:
> http://127.0.0.1:8000

### Telas - Frontend



### Endpoints da API - Back-end

