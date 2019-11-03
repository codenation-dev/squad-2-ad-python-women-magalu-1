# Projeto Final - Central de Erros
# Aceleração Python Woman (Luiza Labs) 
# Squad 2

Para executar o projeto:

### Clonar repositório

Clonar o repositório no seu computador:
```bash
$ cd pasta-desejada
$ git clone https://github.com/codenation-dev/squad-2-ad-python-women-magalu-1.git
```

### Virtualenv

Instalar o Virtualenv:
```bash
$ pip3 install virtualenv
```

### Ambiente virtual

Criar o ambiente virtual com Virtualenv:
```bash
$ cd squad-2-ad-python-women-magalu-1
$ virtualenv venv -p python3
```

Ativar o ambiente virtual:
```bash
$ source venv/bin/activate 
```

Instalar as dependências:
```bash
$ pip3 install -r requirements.txt
```

### Migrations

Criar as migrations
```bash
cd errorcenter
pip3 manage.py makemigrations
pip3 manage.py migrate
```

Criar super usuário
```bash
pip3 manage.py createsuperuser
```

### Tela de Login

Executar o servidor
```bash
pip3 manage.py runserver
```

Acessar a url inicial:
```bash
http://127.0.0.1:8000
```

### Telas - Frontend

### Endpoints da API - Back-end
