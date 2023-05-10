# Desafio 04

## Objetivo

Upar a aplicação para AWS utilizando docker-compose.

## Diretórios

- src/ --> Aplicação
    - Flask/static/ --> Todos os arquivos estáticos do sistema.
        - css/ --> Arquivos .css
        - imagens/ --> Arquivos de imagem.
    
    - Flask/templates/ --> Todos os arquivos .html do sistema.

    - mysql/ --> Dockerfile do MySQL e arquivo .sql para criação das tabelas no container Docker.

## Arquivos
- .gitignore --> Todos os arquivos que devem ser ignorados pelo git.
- app.py --> Instância do flask.
- db.py --> Script que realiza o armazenamento e consulta dos dados enviados para o servidor.
- docker-compose.yml --> Docker compose
- Dockerfile --> Dockerfile Flask e Dockerfile MySQL.
- requirements.txt --> Todos os requerimentos para rodar a aplicação.
- rotas.py --> Onde foram programadas as rotas do sistema.
- setup.sql --> Script SQL que mostra como criar as tabelas do banco de dados, usando MYSQL.

## Requerimentos
**É necessário criar o banco de dados na máquina local para que a aplicação funcione corretamente**

**Para criar as tabelas use o código disponibilizado em src/mysql/setup.sql**

    pip install -r src\requirements.txt

## Rodar o sistema no máquina local
    cd src | flask run

# Rodar o sistema utilizando Docker

**Primeiro envie todos os arquivos da pasta /src para a máquina na AWS**

## Instalando Docker e Docker Compose

    sudo apt update
    sudo apt install docker.io
    sudo apt install docker-compose

## Executando o Docker Compose

**No diretório em que se encontra o arquivo docker-compose.yml**

    docker-compose -f docker-compose.yml up