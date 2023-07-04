from pydantic import BaseModel


class CreateInventory(BaseModel):
    name: str
    price: float
    category: str


class ListInventory(BaseModel):
    data: list[CreateInventory]
