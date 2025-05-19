from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CategoryBase(BaseModel):
    category_name: str
    category_desc: Optional[str] = None


class CategoryCreate(CategoryBase):
    last_updated_by: Optional[str] = None


class CategoryUpdate(BaseModel):
    category_name: Optional[str] = None
    category_desc: Optional[str] = None
    last_updated_by: Optional[str] = None


class CategoryOut(CategoryBase):
    category_id: int
    last_updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
