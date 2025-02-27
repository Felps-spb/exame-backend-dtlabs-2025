from sqlalchemy import Column, String
from app.utils.database import Base

class Server(Base):
    __tablename__ = "servers"
    ulid = Column(String, primary_key=True, index=True) 
    name = Column(String, nullable=False)  