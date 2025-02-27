from fastapi import FastAPI
from app.utils.database import engine, Base
from app.routes.auth import router as auth_router
from app.routes.data import router as data_router
from app.routes.server import router as server_router
from app.routes.health import router as health_router  # Importe as rotas de saúde
from app.models.server import Server  # Importe o modelo Server

app = FastAPI()

# Cria as tabelas no banco de dados (se não existirem)
Base.metadata.create_all(bind=engine)

# Inclui as rotas de autenticação
app.include_router(auth_router, prefix="/auth")

# Inclui as rotas de dados dos sensores
app.include_router(data_router, prefix="")

# Inclui as rotas de servidores
app.include_router(server_router, prefix="")

# Inclui as rotas de monitoramento da saúde
app.include_router(health_router, prefix="")

