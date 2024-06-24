from typing import List

from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

import database
from repository import staff
import schemas

router = APIRouter(prefix='/staff', tags=['Staff'])

#database connection
conn = database.connection


@router.get('/', response_model=List[schemas.Staff])
def get_all(db: Session = Depends(conn)):
    return staff.get_all(db)


# create a Staff
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Staff, db: Session = Depends(conn)):
    return staff.create(request, db)


# get Staff data with id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.Staff)
def get_staff_id(id, db: Session = Depends(conn)):
    return staff.show(id, db)


# delete Staff
# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_staff(id, db: Session = Depends(conn)):
#     return staff.delete(id, db)


# update the Staff
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_staff(id, request: schemas.Staff, db: Session = Depends(conn)):
    return staff.update(id, request, db)
