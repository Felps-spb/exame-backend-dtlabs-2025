from sqlalchemy import Column, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.utils.database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(String, primary_key=True, index=True)
    server_ulid = Column(String, ForeignKey("servers.ulid"), index=True)
    timestamp = Column(DateTime(timezone=True), default=func.now())  # Armazena com fuso horário
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    voltage = Column(Float, nullable=True)
    current = Column(Float, nullable=True)