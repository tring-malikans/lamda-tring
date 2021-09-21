from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class Indicator(BaseModel):
    indi: str = Field(...)
    code: str = Field(...)
    tema1: str = Field(...)
    tema2: str = Field(...)


class IndisModel(BaseModel):
    buy:Optional[Indicator]=None
    sell:Optional[Indicator]=None
    status: bool = Field(...)
    exchange: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "buy":"",
                "sell":"",
                "status": True,
            }
        }


class UpdateIndisModel(BaseModel):
    indicatorname: str = Field(...)
    timeframe: str = Field(...)
    tema1: str = Field(...)
    tema2: str = Field(...)
    status: bool = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "indicatorname":'Tema',
                "timeframe": "5m",
                "tema1": "1",
                "tema2": "2",
                "status": True,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [
            data
        ],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
