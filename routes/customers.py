from typing import List

from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

import database
import oauth2
import schemas
from repository import customers

router = APIRouter(prefix='/customers', tags=['Customers'])

#database connection
conn = database.connection


@router.get('/', response_model=List[schemas.Customers])
def get_all(db: Session = Depends(conn)):
    return customers.get_all(db)


# get_current_user: schemas.Staff = Depends(oauth2.get_current_user)

# create a Customers
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Customers, db: Session = Depends(conn)):
    return customers.create(request, db,)


# get Customers data with id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowCustomers)
def get_customers_id(id, db: Session = Depends(conn)):
    return customers.show(id, db)


# delete Customers
# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_customers(id, db: Session = Depends(conn)):
#     return customers.delete(id, db)


# update the Customers
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_customers(id, request: schemas.Customers, db: Session = Depends(conn)):
    return customers.update(id, request, db)
