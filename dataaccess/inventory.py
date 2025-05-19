from datetime import datetime

from sqlalchemy.orm import Session
from models.inventory import Inventory
from models.inventoryhistory import InventoryHistory
from schema.inventory import InventoryCreate, InventoryUpdate


def get_all_inventory(db: Session):
    return db.query(Inventory).all()


def get_inventory_by_product_id(db: Session, product_id: int):
    return db.query(Inventory).filter(Inventory.product_id == product_id).first()

def get_inventory_history(db: Session):
    return db.query(InventoryHistory).order_by(InventoryHistory.last_updated_at.desc()).all()

def get_low_stock_inventory(db: Session):
    return db.query(Inventory).filter(Inventory.low_stock_bit == True).all()


def update_inventory(db: Session, product_id: int, update_data: InventoryUpdate):
    inventory = get_inventory_by_product_id(db, product_id)
    if inventory:

        history = InventoryHistory(
            product_id=inventory.product_id,
            stock_level=inventory.stock_level,
            stock_threshold=inventory.stock_threshold,
            low_stock_bit=inventory.low_stock_bit,
            last_updated_by=update_data.last_updated_by,
            last_updated_at=datetime.utcnow(),
            change_reason="Stock updated via API"
        )
        db.add(history)

        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(inventory, key, value)
        db.commit()
        db.refresh(inventory)
    return inventory


def create_or_update_inventory(db: Session, data: InventoryCreate):
    inventory = get_inventory_by_product_id(db, data.product_id)
    if inventory:
        return update_inventory(db, data.product_id, data)
    new_inventory = Inventory(**data.dict())
    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory
