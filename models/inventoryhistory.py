from sqlalchemy import Boolean, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship, mapped_column, Mapped
from .base import Base
from typing import Optional
from datetime import datetime

class InventoryHistory(Base):
    __tablename__ = "inventory_history"

    inventory_history_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"), nullable=False)
    stock_level: Mapped[int] = mapped_column(nullable=False)
    stock_threshold: Mapped[int] = mapped_column(nullable=False)
    low_stock_bit: Mapped[bool] = mapped_column(Boolean, default=False)
    last_updated_by: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    last_updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    change_reason: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    product = relationship("Product")
