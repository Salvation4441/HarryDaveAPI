from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

import models
import schemas


# get all productss
def get_all(db: Session):
    category = db.query(models.Category).all()
    return category

def create(request: schemas.Category, db: Session):
    category = models.Category(
        name = request.name
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    # return products
    return {"message": "Category created successfully"}


# delete a product
# def delete(id: int, db: Session):
#     category = db.query(models.Category).filter(models.Category.id == id)
#     if not category.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail="products not found")
#     category.delete(synchronize_session=False)
#     db.commit()
#     return {"message": "products deleted successfully"}


# update a products
def update(id: int, request: schemas.Category, db: Session):
    category = db.query(models.Category).filter(models.Category.id == id)
    if not category.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="products not found")
    category.update(dict(request), synchronize_session=False)
    db.commit()
    return {"message": "products updated successfully"}


# get a products by ID
def show(id: int, db: Session):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="products not found")
    return category

