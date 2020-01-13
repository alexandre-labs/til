from dataclasses import dataclass
import datetime


@dataclass
class Learning:
    """The main model in the TIL"""

    title: str
    description: str
    timestamp: datetime.datetime
