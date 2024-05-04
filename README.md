```markdown
# Sistema de Cobranças Kanastra :moneybag: :computer:

Olá, desenvolvedores! Bem-vindos ao repositório do desafio de contratação da **Kanastra** para a posição de Software Engineer. Este README contém todas as instruções necessárias para vocês testarem a aplicação de cobranças que construímos com muito :heart:.

## :sparkles: Funcionalidades

- **Frontend ReactJS**: Ao acessar a aplicação, você será calorosamente recebido pela tela "Hello Kanastra".
- **Backend Python com FAST API**: Contamos com um endpoint `/charges` robusto que aceita requisições POST para processar e armazenar informações de cobranças.

## :whale: Ambiente Docker

Para garantir que a aplicação funcione perfeitamente no seu ambiente, utilizamos o Docker. Todos os serviços (backend, frontend e banco de dados) são orquestrados via `docker-compose`.

### Pré-requisitos

- Docker instalado e rodando na sua máquina.
- Docker Compose instalado.

### :rocket: Instruções de Execução

1. **Limpeza do Docker**: Antes de tudo, vamos garantir que seu Docker esteja limpo de imagens anteriores para evitar qualquer conflito. Execute o comando:
   ```sh
   docker system prune -a
   ```
   **Atenção**: Este comando removerá todas as imagens não utilizadas. Certifique-se de que está tudo certo antes de prosseguir.

2. **Construção e Execução**: Com o Docker pronto, é hora de construir e executar nossa aplicação:
   ```sh
   docker-compose build
   docker-compose up
   ```
   **Atenção**: Este processo poderá levar de 5 a 15 minutos a depender do seu hardware.

## :globe_with_meridians: Acessando a Aplicação

- **Frontend**: Após os serviços estarem em execução, acesse `http://localhost:8000` e você será redirecionado para a aplicação React.
- **Swagger FASTAPI**: Para testar a API de forma ágil e fácil, utilize o Swagger UI disponível em `http://localhost:8000/docs`.

## :memo: Testando o Endpoint `/charges`

Para enviar uma requisição de teste para o endpoint `/charges`, siga o exemplo de payload abaixo:

```json
{
  "name": "Michelle Mitri",
  "governmentId": "10067798101",
  "email": "example@kanastra.com.br",
  "debtAmount": 990.00,
  "debtDueDate": "26/01/2025"
}
```

## :floppy_disk: Acessando o Banco de Dados MySQL

Para verificar os dados inclusos no banco de dados MySQL, que está rodando em um container Docker, siga os passos abaixo:

1. **Acesso via Docker**: Execute o comando para acessar o container do banco de dados:
   ```sh
   docker exec -it kanatra-database mysql -u root -p
   ```
   Quando solicitado, insira a senha `RootPassword`.

2. **Verificação dos Dados**: Uma vez dentro do MySQL, você pode verificar os dados com os seguintes comandos SQL:
   ```sql
   USE Kanastra;
   SELECT * FROM charges;
   ```
   

Agora é com vocês! Esperamos que tenham uma ótima experiência testando nossa aplicação. Qualquer feedback é bem-vindo! :thumbsup:
```