from typing import List

from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

import database
import oauth2
import schemas
from repository import delivery

router = APIRouter(prefix='/delivery', tags=['Delivery'])

#database connection
conn = database.connection


@router.get('/', response_model=List[schemas.Delivery])
def get_all(db: Session = Depends(conn),get_current_user: schemas.Staff = Depends(oauth2.get_current_user)):
    return delivery.get_all(db)


# create a delivery
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Delivery, db: Session = Depends(conn),get_current_user: schemas.Staff = Depends(oauth2.get_current_user)):
    return delivery.create(request, db)


# get delivery data with id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.DeliveryBase)
def get_delivery_id(id, db: Session = Depends(conn),get_current_user: schemas.Staff = Depends(oauth2.get_current_user)):
    return delivery.show(id, db)


# delete delivery
# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_delivery(id, db: Session = Depends(conn)):
#     return delivery.delete(id, db)


# update the delivery
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_delivery(id, request: schemas.Delivery, db: Session = Depends(conn),get_current_user: schemas.Staff = Depends(oauth2.get_current_user)):
    return delivery.update(id, request, db)
