FROM python:latest

# Definindo variáveis de ambiente ip bd 172.17.0.2
ENV DB_USER=root
ENV DB_PASSWORD=RootPassword
ENV DB_HOST=mysql 
ENV DB_NAME=Kanastra

# Definir o workdir
WORKDIR /code

# Mover o arquivo de dependência do projeto para a pasta code
COPY ./requirements.txt /code/requirements.txt

# Instalar dependências do projeto
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiar a pasta do projeto
COPY ./app /code/app

# Comando para subir o app
CMD ["uvicorn", "app.index:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]