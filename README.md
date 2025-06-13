# Projeto MVP 01 - Puc Rio

## Organizador Financeiro

Organize suas contas de maneira intuitiva e controlada!

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

flask db migrate -m "Criação das tabelas do banco de dados"
flask db upgrade
```

## Aplicação

### Iniciar a aplicação localmente

```bash
flask run
```

### Deploy

Render.com