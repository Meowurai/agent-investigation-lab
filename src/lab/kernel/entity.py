
from abc import ABC
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lab.kernel.id import Identifier

type EntityName = str
type Record = Entity

@dataclass
class Entity(ABC):
    id: Identifier