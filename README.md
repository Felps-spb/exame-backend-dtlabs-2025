# Exame Backend DtLabs 2025

Este é um projeto backend para uma aplicação de IoT, desenvolvido em **Python** com **FastAPI** e **PostgreSQL**, como parte do desafio prático da empresa **DtLabs**.

---

## 📌 Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.9+](https://www.python.org/)

---

## 🚀 Como executar

### 1️⃣ Clone o repositório:
```bash
git clone https://github.com/Felps-spb/exame-backend-dtlabs-2025.git
cd exame-backend-dtlabs-2025
```
---

### 2️⃣ Configure o Ambiente  

Edite o arquivo `.env` caso necessario e configure as variáveis de ambiente:
```env
DATABASE_URL=postgresql://iot_user:iot_password@db:5432/iot_db
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
---
### 3️⃣ Suba a aplicação com Docker
```bash
docker-compose up --build
```

Caso aconteça algum erro na execução do projeto, confira se vc está com o Docker aberto e
se todos os requisitos estão instalados. Suba a aplicação, e verifique se tudo deu certo!

Isso vai:

- 📦 Construir a imagem da aplicação.

- 🛢️ Subir o PostgreSQL em um contêiner Docker.

- 🚀 Inicializar a aplicação FastAPI.

Acesse a *documentação interativa* da API em:

```
http://localhost:8000/docs
```
---

### 🔥 Testando os Endpoints
#### 📝 Registrar usuários
- Endpoint: `POST /auth/register`
- Exemplo de requisição:
  
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "testpassword"
}
```
---
#### 🔑 Fazer login
- Endpoint: `POST /auth/login`
- Exemplo de requisição:
  
```json
{
  "username": "testuser",
  "password": "testpassword"
}
```
Após o login, a API retorna um token JWT. Utilize esse token para acessar os endpoints protegidos.
---

#### 📡 Enviar dados dos sensores
- Endpoint: `POST /data`
- Exemplo de requisição:
  
```json
{
  "server_ulid": "01JN49V9CGGY3XY8STNP1DVHBG",
  "timestamp": "2024-02-19T12:34:56Z",
  "temperature": 25.5,
  "humidity": 60.2,
  "voltage": 220.0,
  "current": 1.5
}
```
---
### 🔍Consultar dados dos sensores
- Endpoint: `GET /data`
- Parâmetros opcionais:
- `server_ulid`
- `start_time`
- `end_time`
- `sensor_type`
- `aggregation`
  
Exemplo de requisição com filtros:
```bash
curl -X GET "http://localhost:8000/data?server_ulid=01JN49V9CGGY3XY8STNP1DVHBG&start_time=2024-02-19T00:00:00Z&end_time=2024-02-19T23:59:59Z" -H "Authorization: Bearer <TOKEN>"
```
---
### 🩺 Verificar a saúde dos servidores
#### ✅ Checar o status de um servidor específico:
- Endpoint: `GET /health/{server_ulid}`
#### 🌍 Checar o status de todos os servidores:
- Endpoint: `GET /health/all`

---
### 🛑 Parar a aplicação

```bash
docker-compose down
```
---
###🧹 Limpar o ambiente (opcional)

- Remova as imagens Docker:
```bash
docker-compose down --rmi all
```
- Remova volumes não utilizados:
```bash
docker volume prune
```
🧪 Executar testes
```bash
pytest
```
---

Pronto! Agora você pode explorar e testar a API. 🚀
Se tiver dúvidas ou precisar de melhorias, sinta-se à vontade para contribuir! 😃
  
