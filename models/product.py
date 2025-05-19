from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from datetime import datetime
from .base import Base

class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_name: Mapped[str] = mapped_column(nullable=False, index=True)
    product_desc: Mapped[Optional[str]] = mapped_column()
    price: Mapped[float] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.category_id"))

    last_updated_by: Mapped[Optional[str]] = mapped_column()
    last_updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    category: Mapped["Category"] = relationship("Category", back_populates="products")
    inventory: Mapped["Inventory"] = relationship("Inventory", back_populates="product", uselist=False)
    sales: Mapped[list["Sale"]] = relationship("Sale", back_populates="product")
