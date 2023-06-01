class Horse:
    """All methods which needs personally to horses"""
    name: str  # horse name
    breed: str  # horse breed
    age: int  # horse age
    color: str  # horse gender
    weight: float  # horse height in hands
    category: str
    areal: str

    def __init__(self, name: str, breed: str, age: int, color: str, weight: float,  category: str, areal: str) -> None:
        """Constructor of the class to set up all basic variables"""
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.weight = weight
        self.category = category
        self.areal = areal
    def get_info(self) -> str:
        """String representation of the object"""
        return f"Horse({self.name}, {self.breed}, {self.age}, {self.color}, {self.weight}, {self.category},{self.areal})"

    def __repr__(self) -> str:
        """String representation of the object"""
        return f"Horse({self.name}, {self.breed}, {self.age}, {self.color}, {self.weight},{self.category},{self.areal})"
