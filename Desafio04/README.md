# ***Desafio 04***

## **Objetivo**

Upar a aplicação para [AWS](https://aws.amazon.com/pt/?nc2=h_lg) utilizando [docker-compose](https://docs.docker.com/compose/).

## **Diretórios**

- [src/](src/) > Aplicação
    - [Flask/static/](src/Flask/static/) > Todos os arquivos estáticos do sistema.
        - [css/](src/Flask/static/css/) > Arquivos .css
        - [imagens/](src/Flask/static/imagens/) > Arquivos de imagem.
    
    - [Flask/templates/](src/Flask/templates/) > Todos os arquivos .html do sistema.

    - [mysql/](src/mysql/) > Dockerfile do MySQL e arquivo .sql para criação das tabelas no container Docker.

## **Arquivos**

- [app.py](src/Flask/app.py) > Instância do flask.
- [db.py](src/Flask/db.py) > Script que realiza o armazenamento e consulta dos dados enviados para o servidor.
- [docker-compose.yml](src/docker-compose.yml) > Docker compose
- Dockerfile > [Dockerfile Flask](src/Flask/Dockerfile) e [Dockerfile MySQL](src/mysql/Dockerfile).
- [requirements.txt](src/Flask/requirements.txt) > Todos os requerimentos para rodar a aplicação.
- [rotas.py](src/Flask/rotas.py) > Onde foram programadas as rotas do sistema.
- [setup.sql](src/mysql/setup.sql) > Script SQL que mostra como criar as tabelas do banco de dados, usando MYSQL.

## **Requerimentos**

**É necessário criar o banco de dados na máquina local para que a aplicação funcione corretamente**

**Para criar as tabelas use o código disponibilizado em src/mysql/setup.sql**

```bash
pip install -r src/requirements.txt
```

## **Rodar o sistema no máquina local**

```bash
cd src | flask run
```

# ***Rodar o sistema utilizando [Docker](https://www.docker.com/)***

**Primeiro envie todos os arquivos da pasta [/src](src/) para a máquina na [AWS](https://aws.amazon.com/pt/?nc2=h_lg)**

## **Instalando [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)**

```bash
sudo apt update
sudo apt install docker.io
sudo apt install docker-compose
```

## **Executando o [Docker Compose](https://docs.docker.com/compose/)**

**No diretório em que se encontra o arquivo [docker-compose.yml](src/docker-compose.yml)**

```bash
docker-compose -f docker-compose.yml up
```