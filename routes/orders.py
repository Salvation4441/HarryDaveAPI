from typing import List
from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session
import database
from repository import orders
import schemas

router = APIRouter(prefix='/orders', tags=['Orders'])

#database connection
conn = database.connection


@router.get('/', response_model=List[schemas.Order])
def get_all(db: Session = Depends(conn)):
    return orders.get_all(db)


# create a Order
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Order, db: Session = Depends(conn)):
    return orders.create(request, db)


# get Order data with id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.OrdersBase)
def get_order_id(id, db: Session = Depends(conn)):
    return orders.show(id, db)


# delete Order
# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_order(id, db: Session = Depends(conn)):
#     return orders.delete(id, db)


# update the Order
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_order(id, request: schemas.Order, db: Session = Depends(conn)):
    return orders.update(id, request, db)
