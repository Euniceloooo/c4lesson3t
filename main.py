from pydantic import BaseModel, field_validator, ValidationError, constr
from typing import Tuple

class IkeaFurniture(BaseModel):
    name: constr(pattern=r'^[\w\s\-\'\,\.]+$')
    dimensions: Tuple[int, int, int]
    material: constr(pattern=r'^[A-Za-z\s/\-]+$')
    price: float

    @field_validator('dimensions')
    @classmethod
    def check_dimensions(cls, v):
        if len(v) != 3 or not all(isinstance(x, int) and x > 0 for x in v):
            raise ValueError('dimensions must be a tuple of three positive integers')
        return v

    @field_validator('price')
    @classmethod
    def check_price(cls, v):
        if v <= 0:
            raise ValueError('price must be positive')
        return v

    def __str__(self):
        return self.name

samples = [
    IkeaFurniture(name='Billy Bookcase', dimensions=(80, 202, 28), material='particle board', price=59.99),
    IkeaFurniture(name='Malm Bed Frame', dimensions=(209, 100, 146), material='wood veneer', price=199.00),
    IkeaFurniture(name='Poäng Armchair', dimensions=(68, 100, 82), material='bentwood', price=79.00),
    IkeaFurniture(name='Kallax Shelf Unit', dimensions=(77, 147, 39), material='fiberboard', price=69.99),
    IkeaFurniture(name='Lack Coffee Table', dimensions=(90, 45, 55), material='fiberboard', price=29.99),
    IkeaFurniture(name='Hemnes Dresser', dimensions=(108, 96, 50), material='solid pine', price=179.00),
    IkeaFurniture(name='Ektorp Sofa', dimensions=(218, 88, 88), material='cotton/polyester', price=399.00),
    IkeaFurniture(name='Alex Desk', dimensions=(131, 76, 60), material='particle board', price=129.00),
    IkeaFurniture(name='Brimnes Wardrobe', dimensions=(78, 190, 50), material='fiberboard', price=149.00),
    IkeaFurniture(name='Markus Office Chair', dimensions=(62, 129, 60), material='mesh/steel', price=229.00)
]

for item in samples:
    print(item)
"""
# Invalid samples
invalid_samples = [
    {"name": "Billy!Bookcase", "dimensions": (80, 202, 28), "material": "particle board", "price": 59.99},  # Invalid name (contains '!')
    {"name": "Malm Bed Frame", "dimensions": [209, 100, 146], "material": "wood veneer", "price": 199.00},   # Invalid dimensions (list, not tuple)
    {"name": "Poäng Armchair", "dimensions": (68, 100, 82), "material": "bentwood", "price": -79.00},       # Invalid price (negative)
]

for idx, args in enumerate(invalid_samples, 1):
    try:
        item = IkeaFurniture(**args)
        print(f"Invalid sample {idx} created: {item}")
    except ValidationError as e:
        print(f"Error for invalid sample {idx}: {e}")
        """