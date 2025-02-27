from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.sensor_data import SensorData
from app.models.server import Server
from datetime import datetime, timedelta 
from app.schemas.sensor_data import SensorDataCreate
from app.schemas.sensor_data import SensorDataQuery, SensorDataAggregatedResponse


def create_sensor_data(db: Session, data: SensorDataCreate):
    """
    Registra os dados dos sensores no banco de dados.
    """
    # Verifica se o servidor existe
    server = db.query(Server).filter(Server.ulid == data.server_ulid).first()
    if not server:
        raise ValueError(f"Servidor com ULID {data.server_ulid} não encontrado")

    # Cria os dados dos sensores
    db_data = SensorData(
        id=data.server_ulid,  # Usando server_ulid como ID temporário (substitua por ULID gerado)
        server_ulid=data.server_ulid,
        timestamp=data.timestamp,
        temperature=data.temperature,
        humidity=data.humidity,
        voltage=data.voltage,
        current=data.current,
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data


def query_sensor_data(db: Session, query: SensorDataQuery):
    """
    Consulta os dados dos sensores com base nos filtros fornecidos.
    """
    # Filtros básicos
    filters = []
    if query.server_ulid:
        filters.append(SensorData.server_ulid == query.server_ulid)
    if query.start_time:
        filters.append(SensorData.timestamp >= query.start_time)
    if query.end_time:
        filters.append(SensorData.timestamp <= query.end_time)

    # Consulta inicial
    data_query = db.query(SensorData).filter(*filters)

    # Agregação de dados
    if query.aggregation:
        if query.aggregation == "minute":
            trunc_func = func.date_trunc("minute", SensorData.timestamp)
        elif query.aggregation == "hour":
            trunc_func = func.date_trunc("hour", SensorData.timestamp)
        elif query.aggregation == "day":
            trunc_func = func.date_trunc("day", SensorData.timestamp)
        else:
            raise ValueError("Tipo de agregação inválido")

        # Seleciona a média dos valores agregados
        data_query = (
            db.query(
                trunc_func.label("timestamp"),
                func.avg(SensorData.temperature).label("temperature"),
                func.avg(SensorData.humidity).label("humidity"),
                func.avg(SensorData.voltage).label("voltage"),
                func.avg(SensorData.current).label("current"),
            )
            .filter(*filters)
            .group_by(trunc_func)
            .order_by(trunc_func)
        )

    # Filtra por tipo de sensor
    if query.sensor_type:
        if query.sensor_type == "temperature":
            data_query = data_query.with_entities(SensorData.timestamp, SensorData.temperature)
        elif query.sensor_type == "humidity":
            data_query = data_query.with_entities(SensorData.timestamp, SensorData.humidity)
        elif query.sensor_type == "voltage":
            data_query = data_query.with_entities(SensorData.timestamp, SensorData.voltage)
        elif query.sensor_type == "current":
            data_query = data_query.with_entities(SensorData.timestamp, SensorData.current)
        else:
            raise ValueError("Tipo de sensor inválido")

    return data_query.all()