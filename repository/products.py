from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

import models
import schemas


# get all productss
def get_all(db: Session):
    products = db.query(models.Products).all()
    return products


def create(request: schemas.Products, db: Session):
    product = models.Products(
        name = request.name,
        description = request.description,
        price = request.price
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    # return products
    return {"message": "Products created successfully"}


# delete a product
# def delete(id: int, db: Session):
#     products = db.query(models.Products).filter(models.Products.id == id)
#     if not products.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail="products not found")
#     products.delete(synchronize_session=False)
#     db.commit()
#     return {"message": "products deleted successfully"}


# update a products
def update(id: int, request: schemas.Products, db: Session):
    products = db.query(models.Products).filter(models.Products.id == id)
    if not products.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="products not found")
    products.update(dict(request), synchronize_session=False)
    db.commit()
    return {"message": "products updated successfully"}


# get a products by ID
def show(id: int, db: Session):
    products = db.query(models.Products).filter(models.Products.id == id).first()
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="products not found")
    return products

