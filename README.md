```markdown
# Sistema de Cobranças Kanastra 💼💻

Olá, desenvolvedores! Bem-vindos ao repositório do desafio de contratação da **Kanastra** para a posição de Software Engineer.
Este README contém todas as instruções necessárias para vocês testarem a aplicação de cobranças que construímos com muito ❤️.

## ✨ Funcionalidades

- **Frontend ReactJS**: Ao acessar a aplicação, você será calorosamente recebido pela tela "Hello Kanastra".
- **Backend Python com FAST API**: Conta com um endpoint `/charges` que aceita requisições POST para processar cobranças.

## 🐳 Ambiente Docker

Para garantir que a aplicação funcione perfeitamente no seu ambiente, utilizamos o Docker.
Todos os serviços (backend, frontend e banco de dados) são orquestrados via `docker-compose`.

### Pré-requisitos

- Docker instalado e rodando na sua máquina.
- Docker Compose instalado.

### 🚀 Instruções de Execução

1. **Limpeza do Docker**: Vamos garantir que seu Docker esteja limpo de imagens para evitar qualquer conflito.
Execute o comando:
   ```sh
      docker system prune -a
   ```

- **Atenção**: Este comando removerá todas as imagens não utilizadas.

2. **Construção e Execução**: Com o Docker pronto, é hora de construir e executar nossa aplicação:
   ```sh
      docker-compose build
      docker-compose up
   ```

## 🌐 Acessando a Aplicação

- **Frontend**: Após os serviços estarem em execução, acesse `http://localhost:8000` e você será redirecionado para a aplicação React.
- **Swagger FASTAPI**: Para testar a API de forma ágil e fácil, utilize o Swagger UI disponível em `http://localhost:8000/docs`.

## 📝 Testando o Endpoint `/charges`

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

## 💾 Acessando o Banco de Dados MySQL

Para verificar os dados inclusos no banco de dados MySQL, que está rodando em um container Docker, siga os passos abaixo:

1. **Acesso via Docker**: Execute o comando para acessar o container do banco de dados:
   ```sh
   docker exec -it kanatra-database mysql -u root -p
   ```
   Quando solicitado, insira a senha `RootPassword`.

2. **Verificação dos Dados**: Uma vez dentro do MySQL, você pode verificar os dados com os seguintes comandos SQL:
   ```sql
   USE Kanastra;
   SELECT * FROM sua_tabela_de_cobrancas;
   ```
   Substitua `sua_tabela_de_cobrancas` pelo nome da tabela onde as cobranças estão sendo armazenadas.

Agora é com vocês! Esperamos que tenham uma ótima experiência testando nossa aplicação. Qualquer feedback é bem-vindo! 👍
```
