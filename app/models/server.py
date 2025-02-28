from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.utils.database import Base

class Server(Base):
    __tablename__ = "servers"

    ulid = Column(String, primary_key=True, index=True)  # ULID do servidor
    name = Column(String, nullable=False)  # Nome do servidor

    # Relacionamento com a tabela sensor_data
    sensor_data = relationship("SensorData", back_populates="server", cascade="all, delete-orphan")