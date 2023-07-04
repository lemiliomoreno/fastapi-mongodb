from bson import ObjectId
from typing import Annotated
from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorDatabase

from models.inventory import CreateInventory, GetInventory
from utils.database import get_db


router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)


@router.get("", response_model=list[GetInventory])
async def list_inventory(database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    inventory_list = [inventory async for inventory in database.inventory.find({})]

    return jsonable_encoder(inventory_list)


@router.post("")
async def create_inventory(
    create_inventory: CreateInventory,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
):
    await database.inventory.insert_one(
        {
            "_id": str(ObjectId()),
            "name": create_inventory.name,
            "price": create_inventory.price,
            "category": create_inventory.category,
        }
    )

    return {"message": "ok"}
