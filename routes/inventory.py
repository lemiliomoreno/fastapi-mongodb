from typing import Annotated
from fastapi import Depends, APIRouter
from motor.motor_asyncio import AsyncIOMotorDatabase

from models.inventory import CreateInventory, ListInventory
from utils.database import get_db


router = APIRouter(
    prefix="/inventory",
    tags=[
        "inventory"
    ],
)


@router.get("", response_model=ListInventory)
async def list_inventory(database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    inventory_list = await database.inventory.find({})

    return inventory_list


@router.post("")
async def create_inventory(create_inventory: CreateInventory, database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    await database.inventory.insert_one({
        "name": create_inventory.name,
        "price": create_inventory.price,
        "category": create_inventory.category,
    })

    return {"message": "ok"}
