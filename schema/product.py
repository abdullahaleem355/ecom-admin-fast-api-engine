from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    product_name: str
    product_desc: Optional[str] = None
    price: float
    category_id: int


class ProductCreate(ProductBase):
    last_updated_by: Optional[str] = None


class ProductUpdate(BaseModel):
    product_name: Optional[str] = None
    product_desc: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None
    last_updated_by: Optional[str] = None


class ProductOut(ProductBase):
    product_id: int
    last_updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
