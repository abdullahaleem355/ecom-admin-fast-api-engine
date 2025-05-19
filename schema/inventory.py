from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InventoryBase(BaseModel):
    product_id: int
    stock_level: int
    stock_threshold: int
    low_stock_bit: bool = False


class InventoryCreate(InventoryBase):
    last_updated_by: Optional[str] = None


class InventoryUpdate(BaseModel):
    stock_level: Optional[int] = None
    stock_threshold: Optional[int] = None
    low_stock_bit: Optional[bool] = None
    last_updated_by: Optional[str] = None


class InventoryOut(InventoryBase):
    inventory_id: int
    last_updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
