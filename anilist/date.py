from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class Date:
    day: int = 0
    month: int = 0
    year: int = 0

    def to_datetime(self) -> datetime:
        return datetime(**self.__dict__, tzinfo=timezone.utc)

    def to_dateint(self) -> str:
        return "{0.year:04}{0.month:02}{0.day:02}".format(self)

    def __str__(self) -> str:
        return f"{self.day or '??'}{self.month or '??'}{self.year or '????'}"