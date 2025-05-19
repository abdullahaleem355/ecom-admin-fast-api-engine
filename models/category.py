from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from datetime import datetime

from .base import Base

class Category(Base):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    category_name: Mapped[str] = mapped_column(nullable=False)
    category_desc: Mapped[Optional[str]] = mapped_column()

    last_updated_by: Mapped[Optional[str]] = mapped_column()
    last_updated_at: Mapped[Optional[datetime]] = mapped_column()

    products: Mapped[list["Product"]] = relationship("Product", back_populates="category")
    sales: Mapped[list["Sale"]] = relationship("Sale", back_populates="category")
