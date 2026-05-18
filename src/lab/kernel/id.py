from dataclasses import dataclass

@dataclass
class IdGenerator:
    counters: dict[str, int] = {}

def next_id(self, name: str) -> str:
    current = self.counters.get(name, 0) + 1
    self.counters[name] = current
    return f"{name}_{current}"

