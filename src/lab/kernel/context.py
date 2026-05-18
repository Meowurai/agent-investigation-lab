

from dataclasses import dataclass
from typing import TYPE_CHECKING

from lab.kernel.id import IdGenerator


if TYPE_CHECKING:
    from lab.kernel.clock import Clock
   
    from random import Random

@dataclass
class Context:
    clock: Clock
    rng: Random
    ids: IdGenerator = IdGenerator()
