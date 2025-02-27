from sqlalchemy.orm import Session
from app.models.server import Server
from app.schemas.server import ServerCreate

def create_server(db: Session, server: ServerCreate):
    """
    Registra um novo servidor no banco de dados.
    """
    db_server = Server(ulid=server.ulid, name=server.name)
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server