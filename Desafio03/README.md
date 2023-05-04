# Desafio 03

## Objetivo

Criar um banco de dados para armazenar as informações enviadas na página de contato a partir do Desafio02.

## Diretórios

- src/ --> Aplicação
    - static/ --> Todos os arquivos estáticos do sistema.
        - css/ --> Arquivos .css
        - imagens/ --> Arquivos de imagem.
    
    - templates/ --> Todos os arquivos .html do sistema.

## Arquivos
- app.py --> Instância do flask.
- rotas.py --> Onde foram programadas as rotas do sistema.
- db.py --> Script que realiza o armazenamento e consulta dos dados enviados para o servidor.
- requirements.txt --> Todos os requerimentos para rodar a aplicação.
- .gitignore --> Todos os arquivos que devem ser ignorados pelo git.
- criacao_do_banco.sql --> Script SQL que mostra como criar o banco de dados, usando MYSQL.

## Requerimentos
    pip install -r src\requirements.txt

## Rodar o sistema
    cd src | flask run