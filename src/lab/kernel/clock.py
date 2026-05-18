from dataclasses import dataclass
from datetime import date, timedelta

@dataclass
class Clock:
    ticks: int
    start_date: date
    delta: timedelta

    current_tick: int  = 1 

    def current_date(self) -> date:
        return self.start_date + (self.delta * (self.current_tick - 1))

    def is_finished(self) -> bool:
        return not self.current_tick <= self.ticks
    
    def advance(self) -> None:
        self.current_tick += 1