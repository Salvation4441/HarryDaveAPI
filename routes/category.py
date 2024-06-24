from typing import List

from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

import database
from repository import category
import schemas

router = APIRouter(prefix='/category', tags=['Categories'])

#database connection
conn = database.connection


@router.get('/', response_model=List[schemas.Category])
def get_all(db: Session = Depends(conn)):
    return category.get_all(db)


# create a products
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Category, db: Session = Depends(conn)):
    return category.create(request, db)


# get products data with id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.Category)
def get_category_id(id, db: Session = Depends(conn)):
    return category.show(id, db)


# delete products
# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_category(id, db: Session = Depends(conn)):
#     return category.delete(id, db)


# update the products
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_category(id, request: schemas.Category, db: Session = Depends(conn)):
    return category.update(id, request, db)
