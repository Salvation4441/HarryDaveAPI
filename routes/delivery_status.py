from typing import List

from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

import database
import schemas
from repository import delivery_status

router = APIRouter(prefix='/delivery_status', tags=['DeliveryStatus'])

#database connection
conn = database.connection


@router.get('/', response_model=List[schemas.DeliveryStatus])
def get_all(db: Session = Depends(conn)):
    return delivery_status.get_all(db)


# create a delivery
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.DeliveryStatus, db: Session = Depends(conn)):
    return delivery_status.create(request, db)


# get delivery data with id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.DeliveryStatusBase)
def get_delivery_id(id, db: Session = Depends(conn)):
    return delivery_status.show(id, db)


# delete delivery
# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_delivery(id, db: Session = Depends(conn)):
#     return delivery.delete(id, db)


# update the delivery
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_delivery(id, request: schemas.DeliveryStatus, db: Session = Depends(conn)):
    return delivery_status.update(id, request, db)
