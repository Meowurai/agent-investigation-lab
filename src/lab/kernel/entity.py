
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from lab.kernel.id import Identifier

type Visibility = Literal["observed", "hidden", "both"]

@dataclass
class Entity:
    id: Identifier = field(metadata={
        "visibility": "both",
        "description": "Unique entity identifier.",
        "example": "customer_1"
    })