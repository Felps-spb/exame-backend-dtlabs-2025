from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.sensor_data import SensorDataCreate, SensorDataResponse
from app.services.data_service import create_sensor_data, query_sensor_data
from app.utils.database import get_db
from app.utils.jwt_handler import verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemas.sensor_data import SensorDataAggregatedResponse, SensorDataQuery
from datetime import datetime
from typing import Optional

router = APIRouter()

@router.post("/data", response_model=SensorDataResponse)
def register_sensor_data(data: SensorDataCreate, db: Session = Depends(get_db)):
    """
    Endpoint para registrar dados dos sensores.
    """
    # Verifica se pelo menos um sensor foi enviado
    if not any([data.temperature, data.humidity, data.voltage, data.current]):
        raise HTTPException(status_code=400, detail="Pelo menos um sensor deve ser enviado")

    try:
        # Registra os dados no banco de dados
        db_data = create_sensor_data(db, data)
        return db_data
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

        
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

@router.get("/data", response_model=list[SensorDataAggregatedResponse])
def get_sensor_data(
    server_ulid: Optional[str] = None,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
    sensor_type: Optional[str] = None,
    aggregation: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),  # Exige autenticação JWT
):
    """
    Endpoint para consultar dados dos sensores.
    """
    query = SensorDataQuery(
        server_ulid=server_ulid,
        start_time=start_time,
        end_time=end_time,
        sensor_type=sensor_type,
        aggregation=aggregation,
    )

    try:
        data = query_sensor_data(db, query)
        return data
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))