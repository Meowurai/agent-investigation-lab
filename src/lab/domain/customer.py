
from dataclasses import dataclass, field

from lab.kernel.entity import Entity

@dataclass
class Customer(Entity):
    product_fit: float = field(metadata={
        "visibility": "hidden",
        "description": "Hidden true fit between customer and product (0-1).",
        "example": 0.72,
    })

    frustration: float = field(metadata={
        "visibility": "hidden",
        "description": "Hidden true customer frustration level (0-1).",
        "example": 0.61,
    })

    churned: bool = field(metadata={
        "visibility": "both",
        "description": "If customer has churned.",
        "example": True
    })