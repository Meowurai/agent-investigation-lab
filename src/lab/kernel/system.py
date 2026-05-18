
from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lab.kernel.context import Context
    from lab.kernel.state import State
    from lab.kernel.event import Event 


class SystemType(Enum):
    BEHAVIOR = "behavior"
    PRESSURE = "pressure"

@dataclass
class System(ABC):
    type: SystemType

    @abstractmethod
    def emit(self, context: Context, state: State) -> list[Event]:
        ...