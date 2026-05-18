

from dataclasses import dataclass
from random import Random

from lab.kernel.clock import Clock

@dataclass
class Context:
    clock: Clock
    rng: Random
