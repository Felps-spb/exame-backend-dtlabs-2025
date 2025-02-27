from pydantic import BaseModel

class ServerHealthResponse(BaseModel):
    server_ulid: str
    status: str
    server_name: str

class AllServersHealthResponse(BaseModel):
    servers: list[ServerHealthResponse]