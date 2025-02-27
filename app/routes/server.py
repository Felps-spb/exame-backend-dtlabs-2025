from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.server import ServerCreate, ServerResponse
from app.services.server_service import create_server
from app.utils.database import get_db

router = APIRouter()

@router.post("/servers", response_model=ServerResponse)
def register_server(server: ServerCreate, db: Session = Depends(get_db)):
    """
    Endpoint para registrar um novo servidor.
    """
    db_server = create_server(db, server)
    return db_server