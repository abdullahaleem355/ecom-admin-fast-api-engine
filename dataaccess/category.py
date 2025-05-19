from sqlalchemy.orm import Session
from models.category import Category
from schema.category import CategoryCreate, CategoryUpdate


def get_all_categories(db: Session):
    return db.query(Category).all()


def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.category_id == category_id).first()


def create_category(db: Session, category_data: CategoryCreate):
    category = Category(**category_data.dict())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def update_category(db: Session, category_id: int, update_data: CategoryUpdate):
    category = get_category_by_id(db, category_id)
    if category:
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(category, key, value)
        db.commit()
        db.refresh(category)
    return category
