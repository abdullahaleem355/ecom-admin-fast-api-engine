from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import SaleCreate, SaleOut
from dataaccess import sale as sales_crud
from database import get_db
from typing import List
from datetime import date

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/", response_model=SaleOut)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    return sales_crud.create_sale(db, sale)


@router.get("/", response_model=List[SaleOut])
def get_sales(start_date: date, end_date: date, product_id: int = None, category_id: int = None, db: Session = Depends(get_db)):
    return sales_crud.get_sales(db, start_date, end_date, product_id, category_id)

@router.get("/revenue/daily")
def get_weekly_revenue(start_date: date, end_date: date, db: Session = Depends(get_db)):
    return sales_crud.get_revenue_by_time(db, start_date, end_date, "daily")


@router.get("/revenue/weekly")
def get_weekly_revenue(start_date: date, end_date: date, db: Session = Depends(get_db)):
    return sales_crud.get_revenue_by_time(db, start_date, end_date, "weekly")


@router.get("/revenue/monthly")
def get_monthly_revenue(start_date: date, end_date: date, db: Session = Depends(get_db)):
    return sales_crud.get_revenue_by_time(db, start_date, end_date, "monthly")


@router.get("/revenue/annual")
def get_annual_revenue(start_date: date, end_date: date, db: Session = Depends(get_db)):
    return sales_crud.get_revenue_by_time(db, start_date, end_date, "annual")


@router.get("/revenue/custom-range")
def get_custom_revenue(start_date: date, end_date: date, db: Session = Depends(get_db)):
    return sales_crud.get_revenue_by_time(db, start_date, end_date, "custom")
