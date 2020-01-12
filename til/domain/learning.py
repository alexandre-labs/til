import datetime
from pydantic import BaseModel


class Learning(BaseModel):
    """The main model in the TIL"""

    title: str
    description: str
    timestamp: datetime.datetime

    class Config:
        strict_models = True
