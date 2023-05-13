# ***Desafio 02***

## **Objetivo**

Hospedar o desafio 01 no flask, mini-framework do Python.

## **Diretórios**

- [src/](src/) > Aplicação
    - [static/](src/static/) > Todos os arquivos estáticos do sistema.
        - [css/](src/static/css/) > Arquivos .css
        - [imagens/](src/static/imagens/) > Arquivos de imagem.
    
    - [templates/](src/templates/) > Todos os arquivos .html do sistema.

## **Arquivos**

- [app.py](src/app.py) > Instância do flask.
- [rotas.py](src/rotas.py) > Onde foram programadas as rotas do sistema.
- [requirements.txt](src/requirements.txt) > Todos os requerimentos para rodar a aplicação.

## **Requerimentos**

```bash 
pip install -r src/requirements.txt
```

## **Rodar o sistema**

```bash
cd src | flask run
```