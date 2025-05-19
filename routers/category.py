from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema import CategoryCreate, CategoryUpdate, CategoryOut
from dataaccess import category as category_crud
from database import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryOut)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return category_crud.create_category(db, category)


@router.get("/{category_id}", response_model=CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = category_crud.get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.put("/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    return category_crud.update_category(db, category_id, category)


@router.get("/", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    return category_crud.get_all_categories(db)
