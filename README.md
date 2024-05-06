# Sistema de Cobranças Kanastra 💼💻 - Hiring Challenge

Olá, desenvolvedores! Me chamo Aparício Junior e estou participando do processo seletivo "Programa de aceleração Tech".
Bem-vindos ao repositório do desafio de contratação da **Kanastra** para a posição de Software Engineer.
Este README contém todas as informações e instruções necessárias.

## ✨ Funcionalidades

- **Frontend ReactJS**: Ao acessar a aplicação, você será calorosamente recebido pela tela "Hello Kanastra".
- **Backend Python com FAST API**: Conta com um endpoint `/charges` que aceita requisições POST para processar cobranças.
- **Modelagem de Banco de Dados MySQL**: Conta com scripts feitos com MySQL para modelar e salvar as requisições provindas da API.

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

3. **Desmontando e parando containeres (a critério de conhecimento, não pare-os agora)**
   ```sh
   docker-compose down
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
   SELECT * FROM charges;
   ```

   ## 🧪 Testes Unitários com Pytest, UnitTest e Coverage

Para assegurar a qualidade e o correto funcionamento das funcionalidades do sistema, é essencial realizar testes unitários. Siga os comandos abaixo para executar os testes no ambiente Docker:

1. **Listagem de Containers**: Verifique os containers em execução para identificar o ID do container `kanastra-backend`:
   ```sh
   docker ps
   ```

2. **Acesso ao Container**: Utilize o ID obtido para acessar o bash do container `kanastra-backend`:
   ```sh
   docker exec -it <ID do kanastra-backend> bash
   ```

3. **Execução dos Testes**: Dentro do container, execute os testes com o `pytest`:
   ```sh
   coverage run -m pytest -vv
   ```

4. **Relatório de Cobertura**: Após a execução dos testes, gere o relatório de cobertura:
   ```sh
   coverage report -m
   ```

5. **Relatório HTML**: Para uma visualização mais detalhada e formatada, gere o relatório em HTML:
   ```sh
   coverage html
   ```

## 📬 Seção de Contato 

Para qualquer dúvida, feedback ou se você simplesmente quer bater um papo, não hesite em entrar em contato comigo! Aqui estão as informações para que você possa me encontrar:

- **Email**: [apariciojunior11@gmail.com](mailto:apariciojunior11@gmail.com)
- **LinkedIn**: [Aparício Junior](https://www.linkedin.com/in/apariciojunior)
- **Curso**: Sistemas para Internet
- **Período**: 5º Semestre

Estou sempre aberto a novas conexões e oportunidades de aprendizado. Vamos conversar! 💼🎓🚀
