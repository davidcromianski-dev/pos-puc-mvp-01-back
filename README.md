# Projeto MVP 01 - Puc Rio

## Organizador Financeiro

Organize suas contas de maneira intuitiva e controlada!

## Tecnologias do Back-end

- Python
- Flask
- Flask OpenAPI
- Flask SQLAlchemy
- Flask CORS
- SQLite

## Iniciar ambiente virtual (venv)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux

```bash
apt install python3.12-venv # Em distros baseadas em Debian/Ubuntu
python3 -m venv venv
source venv/bin/activate
```

## Instalar as depedências

Utilizando o gerenciador `pip`, execute no terminal:

```bash
pip install -r requirements.txt
```

## Construir o Banco de dados

Para o banco de dados, utilizo a biblioteca SQLAlchemy, que atua como um ORM gerenciando todas as operações com o banco.

### Iniciar o banco e criar tabelas

O banco de dados está sendo criado em `/database/finances.db` e as migrations, estão na pasta `/migrations`.

IMPORTANTE! Para executa as migrações, precisa ter o FLASK mapeado no seu sistema operacional:

```bash
# Linux/macOS
export FLASK_APP=run.py

# Windows CMD
set FLASK_APP=run.py

# PowerShell
$env:FLASK_APP = "run.py"
```

```bash
# SOMENTE 1x
flask db init
mkdir database
flask db migrate -m "Criação das tabelas do banco de dados"
flask db upgrade
```

## Aplicação

### Iniciar a aplicação localmente

```bash
flask run
```

### Iniciar utilizando o init

Linux

```bash
sudo bash init.sh
```

Windows

```bash
.\script.bat
```