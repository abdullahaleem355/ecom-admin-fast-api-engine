from sqlalchemy.orm import Session
from models.sale import Sale
from schema.sale import SaleCreate
from sqlalchemy import and_, extract
from datetime import date


def get_sales(db: Session, start_date: date = None, end_date: date = None, product_id: int = None, category_id: int = None):
    query = db.query(Sale)

    if start_date:
        query = query.filter(Sale.sale_date >= start_date)
    if end_date:
        query = query.filter(Sale.sale_date <= end_date)
    if product_id:
        query = query.filter(Sale.product_id == product_id)
    if category_id:
        query = query.filter(Sale.category_id == category_id)

    return query.all()


def get_revenue_by_time(db: Session, start_date: date, end_date: date, time_unit: str):
    query = db.query(Sale).filter(and_(Sale.sale_date >= start_date, Sale.sale_date <= end_date))

    if time_unit == "weekly":
        return query.group_by(extract('week', Sale.sale_date)).all()
    elif time_unit == "monthly":
        return query.group_by(extract('month', Sale.sale_date)).all()
    elif time_unit == "annual":
        return query.group_by(extract('year', Sale.sale_date)).all()
    else:
        return query.all()


def create_sale(db: Session, sale_data: SaleCreate):
    sale = Sale(**sale_data.dict())
    db.add(sale)
    db.commit()
    db.refresh(sale)
    return sale
