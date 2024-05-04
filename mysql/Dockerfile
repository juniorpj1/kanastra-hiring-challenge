# Derivando da imagem oficial do MySQL
FROM mysql:latest

# Adicionando um database
ENV MYSQL_DATABASE Kanastra

# Adicionando os scripts SQL para serem executados na criação do banco
COPY ./database/ /docker-entrypoint-initdb.d/