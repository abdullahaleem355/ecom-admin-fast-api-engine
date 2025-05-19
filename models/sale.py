from datetime  import datetime
from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from . import Product, Category
from .base import Base
from typing import Optional

class Sale(Base):
    __tablename__ = "sales"

    sale_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    sale_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    product_id: Mapped[Optional[int]] = mapped_column(ForeignKey("products.product_id"))
    category_id: Mapped[Optional[int]] = mapped_column(ForeignKey("categories.category_id"))

    quantity: Mapped[int] = mapped_column(nullable=False)
    amount_processed: Mapped[float] = mapped_column(nullable=False)
    revenue: Mapped[float] = mapped_column(nullable=False)

    last_updated_by: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    last_updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    product: Mapped["Product"] = relationship("Product", back_populates="sales")
    category: Mapped["Category"] = relationship("Category", back_populates="sales")
