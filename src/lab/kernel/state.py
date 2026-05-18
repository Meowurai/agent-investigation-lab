
from dataclasses import dataclass
from collections import defaultdict

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lab.kernel.event import Event
    from lab.kernel.entity import Entity, EntityName, Record

@dataclass
class State:
    events: list[Event] = []
    data: dict[EntityName, list[Entity]] = defaultdict(list)

    def add_record(self, record: Record) -> None:
        self.data[record.__class__.__name__].append(record)