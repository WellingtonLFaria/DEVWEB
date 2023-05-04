# Desafio 03

## Objetivo

Upar a aplicação para AWS.

## Diretórios

- src/ --> Aplicação
    - static/ --> Todos os arquivos estáticos do sistema.
        - css/ --> Arquivos .css
        - imagens/ --> Arquivos de imagem.
    
    - templates/ --> Todos os arquivos .html do sistema.

## Arquivos
- .gitignore --> Todos os arquivos que devem ser ignorados pelo git.
- app.py --> Instância do flask.
- db.py --> Script que realiza o armazenamento e consulta dos dados enviados para o servidor.
- docker-compose.yml --> Docker compose
- Dockerfile --> Dockerfile Flask
- requirements.txt --> Todos os requerimentos para rodar a aplicação.
- rotas.py --> Onde foram programadas as rotas do sistema.
- setup.sql --> Script SQL que mostra como criar o banco de dados, usando MYSQL.

## Requerimentos
    pip install -r src\requirements.txt

## Rodar o sistema no máquina local
    cd src | flask run