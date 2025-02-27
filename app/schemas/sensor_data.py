from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SensorDataCreate(BaseModel):
    server_ulid: str
    timestamp: datetime
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    voltage: Optional[float] = None
    current: Optional[float] = None

class SensorDataResponse(BaseModel):
    id: str
    server_ulid: str
    timestamp: datetime
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    voltage: Optional[float] = None
    current: Optional[float] = None

    class Config:
        from_attributes = True

class SensorDataQuery(BaseModel):
    server_ulid: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    sensor_type: Optional[str] = None
    aggregation: Optional[str] = None

class SensorDataAggregatedResponse(BaseModel):
    timestamp: datetime
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    voltage: Optional[float] = None
    current: Optional[float] = None