from models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name) -> None:
        super().__init__()
        self.name: str = name

    def __str__(self) -> str:
        return f"Amenity: {self.name}"
