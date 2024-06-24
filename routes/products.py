from typing import List

from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

import database
from repository import products
import schemas

router = APIRouter(prefix='/products', tags=['Products'])

#database connection
conn = database.connection


@router.get('/', response_model=List[schemas.ProductsBase])
def get_all(db: Session = Depends(conn)):
    return products.get_all(db)


# create a products
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Products, db: Session = Depends(conn)):
    return products.create(request, db)


# get products data with id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ProductsBase)
def get_products_id(id, db: Session = Depends(conn)):
    return products.show(id, db)


# delete products
# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_products(id, db: Session = Depends(conn)):
#     return products.delete(id, db)


# update the products
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_products(id, request: schemas.Products, db: Session = Depends(conn)):
    return products.update(id, request, db)
