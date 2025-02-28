from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.health import ServerHealthResponse, AllServersHealthResponse
from app.services.health_service import get_server_health, get_all_servers_health
from app.utils.database import get_db
from app.utils.jwt_handler import verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Verifica se o token JWT é válido e retorna o payload.
    """
    token = credentials.credentials
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    return payload

@router.get("/health/all", response_model=AllServersHealthResponse)
def get_all_servers_status(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """
    Endpoint para verificar o status de todos os servidores.
    """
    try:
        servers_health = get_all_servers_health(db)
        return servers_health
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/health/{server_ulid}", response_model=ServerHealthResponse)
def get_server_status(
    server_ulid: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """
    Endpoint para verificar o status de um servidor.
    """
    try:
        server_health = get_server_health(db, server_ulid)
        return server_health
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))