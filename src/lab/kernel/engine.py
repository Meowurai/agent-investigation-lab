
from dataclasses import dataclass
from datetime import date, timedelta

from lab.kernel.clock import Clock

@dataclass
class RunConfig:
    ticks: int 
    start_date: date 
    delta: timedelta
    seed: int

class Engine:
    def run(self, config: RunConfig) -> None:
        clock = Clock(
            config.ticks,
            config.start_date,
            config.delta
        )

        while not clock.is_finished():
            print(clock.current_date())
            clock.advance()

if __name__ == "__main__":
    
    engine = Engine()

    config = RunConfig(
        ticks=3, 
        start_date=date(2026, 1, 1), 
        delta=timedelta(days=1),
        seed=42
    )

    engine.run(config)