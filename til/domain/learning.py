import datetime
from pydantic.dataclasses import dataclass


@dataclass
class Learning:
    """The main model in the TIL"""
    title: str
    description: str
    timestamp: datetime.datetime
