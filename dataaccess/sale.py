from sqlalchemy.orm import Session
from models.sale import Sale
from schema.sale import SaleCreate
from sqlalchemy import and_, extract, func
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
    query = db.query(
        func.sum(Sale.revenue).label("total_revenue")
    ).filter(
        and_(Sale.sale_date >= start_date, Sale.sale_date <= end_date)
    )
    if time_unit == "daily":
        query = query.add_columns(Sale.sale_date).group_by(Sale.sale_date)
    elif time_unit == "weekly":
        query = query.add_columns(extract('week', Sale.sale_date).label("week")).group_by("week")
    elif time_unit == "monthly":
        query = query.add_columns(extract('month', Sale.sale_date).label("month")).group_by("month")
    elif time_unit == "annual":
        query = query.add_columns(extract('year', Sale.sale_date).label("year")).group_by("year")

    results = query.all()
    response = []
    for row in results:
        if time_unit == "daily":
            response.append({"date": row.sale_date, "total_revenue": row.total_revenue})
        elif time_unit == "weekly":
            response.append({"week": row.week, "total_revenue": row.total_revenue})
        elif time_unit == "monthly":
            response.append({"month": row.month, "total_revenue": row.total_revenue})
        elif time_unit == "annual":
            response.append({"year": row.year, "total_revenue": row.total_revenue})
        else:
            response.append({"total_revenue": row.total_revenue})
    return response


def create_sale(db: Session, sale_data: SaleCreate):
    sale = Sale(**sale_data.dict())
    db.add(sale)
    db.commit()
    db.refresh(sale)
    return sale
