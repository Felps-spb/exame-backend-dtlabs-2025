from pydantic import BaseModel

class ServerCreate(BaseModel):
    ulid: str
    name: str

class ServerResponse(BaseModel):
    ulid: str
    name: str

    class Config:
        from_attributes = True