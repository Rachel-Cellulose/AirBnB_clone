from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, email, password, first_name, last_name) -> None:
        super().__init__()
        self.email: str = email
        self.password: str = password
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self) -> str:
        return f"User: {self.name} - {self.age}"
