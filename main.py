import re

class IkeaFurniture:

    def __init__(self, name, dimensions, material, price):
        # Regex patterns
        name_pattern = r'^[\w\s\-\'\,\.]+$'  # Letters, numbers, spaces, hyphens, apostrophes, commas, periods
        material_pattern = r'^[A-Za-z\s/\-]+$'  # Letters, spaces, slashes, hyphens
        # Validate name
        if not re.match(name_pattern, name):
            raise ValueError(f"Invalid name: {name}")
        # Validate dimensions: tuple of 3 positive integers
        if not (isinstance(dimensions, tuple) and len(dimensions) == 3 and all(isinstance(x, int) and x > 0 for x in dimensions)):
            raise ValueError(f"Invalid dimensions: {dimensions}")
        # Validate material
        if not re.match(material_pattern, material):
            raise ValueError(f"Invalid material: {material}")
        # Validate price: positive float or int
        if not (isinstance(price, (int, float)) and price > 0):
            raise ValueError(f"Invalid price: {price}")
        self.name = name # variable, object attribut
        self.dimensions = dimensions  # dimensions should be a tuple (width, height, depth)
        self.material = material
        self.price = price

    def __str__(self):
        return(self.name)

sample = IkeaFurniture('bookcase', (20,200,30), 'particle board', 199.99)

samples = [
    IkeaFurniture('Billy Bookcase', (80, 202, 28), 'particle board', 59.99),
    IkeaFurniture('Malm Bed Frame', (209, 100, 146), 'wood veneer', 199.00),
    IkeaFurniture('Poäng Armchair', (68, 100, 82), 'bentwood', 79.00),
    IkeaFurniture('Kallax Shelf Unit', (77, 147, 39), 'fiberboard', 69.99),
    IkeaFurniture('Lack Coffee Table', (90, 45, 55), 'fiberboard', 29.99),
    IkeaFurniture('Hemnes Dresser', (108, 96, 50), 'solid pine', 179.00),
    IkeaFurniture('Ektorp Sofa', (218, 88, 88), 'cotton/polyester', 399.00),
    IkeaFurniture('Alex Desk', (131, 76, 60), 'particle board', 129.00),
    IkeaFurniture('Brimnes Wardrobe', (78, 190, 50), 'fiberboard', 149.00),
    IkeaFurniture('Markus Office Chair', (62, 129, 60), 'mesh/steel', 229.00)
]

for item in samples:
    print(item)

# Invalid samples
invalid_samples = [
    ("Billy!Bookcase", (80, 202, 28), "particle board", 59.99),  # Invalid name (contains '!')
    ("Malm Bed Frame", [209, 100, 146], "wood veneer", 199.00),   # Invalid dimensions (list, not tuple)
    ("Poäng Armchair", (68, 100, 82), "bentwood", -79.00),       # Invalid price (negative)
]

for idx, args in enumerate(invalid_samples, 1):
    try:
        item = IkeaFurniture(*args)
        print(f"Invalid sample {idx} created: {item}")
    except ValueError as e:
        print(f"Error for invalid sample {idx}: {e}")