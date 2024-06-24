from typing import List

from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

import database
from repository import staff, user
import schemas

router = APIRouter(prefix='/user',tags=['Users'])

#database connection
conn = database.connection


# creating user
@router.post('/', response_model=schemas.Staff)
def create_user(request: schemas.Staff, db: Session = Depends(conn)):
    return user.register(request, db)


# get user by id
@router.get('/{id}', response_model=schemas.Staff)
def get_user(id, db: Session = Depends(conn)):
    return (user.show_staff_by_id(id, db))


# get all users
@router.get('/', response_model=List[schemas.Staff])
def show_all_users(db: Session = Depends(conn)):
    return user.show_Staffs(db)
