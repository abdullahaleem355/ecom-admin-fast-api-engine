from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import Product
from schema import ProductUpdate, ProductOut
from dataaccess import product as product_crud
from database import get_db

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    return product_crud.update_product(db, product_id, product)


@router.get("/", response_model=list[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return product_crud.get_products(db)
