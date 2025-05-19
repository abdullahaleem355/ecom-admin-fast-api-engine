from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SaleBase(BaseModel):
    sale_date: datetime
    product_id: int
    quantity: int
    amount_processed: float
    revenue: float
    category_id: int


class SaleCreate(SaleBase):
    last_updated_by: Optional[str] = None


class SaleOut(SaleBase):
    sale_id: int
    last_updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
