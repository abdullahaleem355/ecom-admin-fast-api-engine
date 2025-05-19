from sqlalchemy import Boolean, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .base import Base
from typing import Optional
from datetime import datetime

class Inventory(Base):
    __tablename__ = "inventories"

    inventory_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"), nullable=False)
    stock_level: Mapped[int] = mapped_column(nullable=False)
    stock_threshold: Mapped[int] = mapped_column(nullable=False)
    low_stock_bit: Mapped[bool] = mapped_column(Boolean, default=False)

    last_updated_by: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    last_updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    product = relationship("Product", back_populates="inventory")
