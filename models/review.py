#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, place_id, user_id, text) -> None:
        super().__init__()
        self.place_id: str = place_id
        self.user_id: str = user_id
        self.text: str = text

    def __str__(self) -> str:
        return f"Review: {self.text}"
