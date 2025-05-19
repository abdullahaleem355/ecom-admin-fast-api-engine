from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InventoryHistoryOut(BaseModel):
    inventory_history_id: int
    product_id: int
    stock_level: int
    stock_threshold: int
    low_stock_bit: bool
    last_updated_by: Optional[str]
    last_updated_at: Optional[datetime]
    change_reason: Optional[str]

    class Config:
        orm_mode = True
