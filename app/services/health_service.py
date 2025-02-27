from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone 
from app.models.server import Server
from app.models.sensor_data import SensorData
from app.schemas.health import ServerHealthResponse, AllServersHealthResponse

def get_server_health(db: Session, server_ulid: str):
    """
    Verifica a saúde de um servidor com base no último dado recebido.
    """
    server = db.query(Server).filter(Server.ulid == server_ulid).first()
    if not server:
        raise ValueError(f"Servidor com ULID {server_ulid} não encontrado")

    # Verifica o último dado recebido
    last_data = (
        db.query(SensorData)
        .filter(SensorData.server_ulid == server_ulid)
        .order_by(SensorData.timestamp.desc())
        .first()
    )

    # Define o status do servidor
    if last_data:
        # Converte o timestamp para offset-aware (UTC)
        last_data_timestamp = last_data.timestamp.replace(tzinfo=timezone.utc)
        # Obtém o tempo atual em UTC (offset-aware)
        current_time = datetime.now(timezone.utc)
        # Verifica se o último dado foi recebido há menos de 10 segundos
        if (current_time - last_data_timestamp) <= timedelta(seconds=10):
            status = "online"
        else:
            status = "offline"
    else:
        status = "offline"

    return ServerHealthResponse(
        server_ulid=server.ulid,
        status=status,
        server_name=server.name,
    )

def get_all_servers_health(db: Session):
    """
    Verifica a saúde de todos os servidores.
    """
    servers = db.query(Server).all()
    servers_health = []

    for server in servers:
        server_health = get_server_health(db, server.ulid)
        servers_health.append(server_health)

    return AllServersHealthResponse(servers=servers_health)