from models.base_model import BaseModel


class City(BaseModel):
    def __init__(self, name, state_id) -> None:
        super().__init__()
        self.name: str = name
        self.state_id: str = state_id

    def __str__(self) -> str:
        return f"City: {self.name}"
