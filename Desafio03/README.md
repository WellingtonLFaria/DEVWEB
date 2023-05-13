# ***Desafio 03***

## **Objetivo**

Criar um banco de dados para armazenar as informações enviadas na página de contato a partir do Desafio02.

## **Diretórios**

- [src/](src/) > Aplicação
    - [static/](src/static/) > Todos os arquivos estáticos do sistema.
        - [css/](src/static/css/) > Arquivos .css
        - [imagens/](src/static/imagens/) > Arquivos de imagem.
    
    - [templates/](src/templates/) --> Todos os arquivos .html do sistema.

## **Arquivos**
- [app.py](src/app.py) > Instância do flask.
- [rotas.py](src/rotas.py) > Onde foram programadas as rotas do sistema.
- [db.py](src/db.py) > Script que realiza o armazenamento e consulta dos dados enviados para o servidor.
- [requirements.txt](src/requirements.txt) > Todos os requerimentos para rodar a aplicação.
- [criacao_do_banco.sql](src/criacao_do_banco.sql) > Script SQL que mostra como criar o banco de dados, usando MYSQL.

## **Requerimentos**

```bash
pip install -r src/requirements.txt
```

## **Rodar o sistema**
    
```bash
cd src | flask run
```