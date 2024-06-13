from pydantic import BaseModel
from typing import Dict, Any

class ConfigurationCreate(BaseModel):
    country_code: str
    requirements: Dict[str, Any]

class ConfigurationUpdate(BaseModel):
    requirements: Dict[str, Any]

class Configuration(BaseModel):
    id: int
    country_code: str
    requirements: Dict[str, Any]

    class Config:
        orm_mode = True
