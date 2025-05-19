from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema import InventoryCreate, InventoryUpdate, InventoryOut
from dataaccess import inventory as inventory_crud
from database import get_db
from schema.inventoryhistory import InventoryHistoryOut

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/", response_model=list[InventoryOut])
def get_all_inventory(db: Session = Depends(get_db)):
    return inventory_crud.get_all_inventory(db)

@router.get("/low", response_model=list[InventoryOut])
def get_low_stock_items(db: Session = Depends(get_db)):
    return inventory_crud.get_low_stock_inventory(db)


@router.post("/{product_id}", response_model=InventoryOut)
def update_inventory(product_id: int, inventory: InventoryUpdate, db: Session = Depends(get_db)):
    updated_inventory = inventory_crud.update_inventory(db, product_id, inventory)
    if not updated_inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return updated_inventory


@router.get("/history", response_model=list[InventoryHistoryOut])
def get_inventory_history(db: Session = Depends(get_db)):
    return inventory_crud.get_inventory_history(db)


@router.get("/{product_id}", response_model=InventoryOut)
def get_inventory_by_product_id(product_id: int, db: Session = Depends(get_db)):
    inventory = inventory_crud.get_inventory_by_product_id(db, product_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory


