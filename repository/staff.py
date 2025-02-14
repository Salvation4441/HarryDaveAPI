from sqlalchemy.orm import Session
from fastapi import  status, HTTPException

import models
import schemas
from hashing import Hash


# get all Staffs
def get_all(db: Session):
    staff = db.query(models.Staff).all()
    return staff


def create(request: schemas.Staff, db: Session):
    # Check if the user already exists
    exiting_user = db.query(models.Staff).filter(models.Staff.email == request.email).first()
    if exiting_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User with this email already exists")
    staff = models.Staff(
        firstname=request.firstname,
        lastname = request.lastname,
        password= Hash.bcrypt(request.password),
        email = request.email,
        phone = request.phone,
        role = request.role,
        card_number= request.card_number,
    )
    db.add(staff)
    db.commit()
    db.refresh(staff)
    # return Staff
    return {"message": "Staff created successfully"}


# delete a Staff
# def delete(id: int, db: Session):
#     staff = db.query(models.Staff).filter(models.Staff.id == id)
#     if not staff.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Staff with id {id} not found")
#     staff.delete(synchronize_session=False)
#     db.commit()
#     return {"message": f"Staff with id {id} deleted successfully"}


# update a Staff
def update(id: int, request: schemas.Staff, db: Session):
    staff = db.query(models.Staff).filter(models.Staff.id == id)
    if not staff.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Staff with ID {id} not found")
    staff.update(dict(request), synchronize_session=False)
    db.commit()
    return {"message": "Staff updated successfully"}


# get a Staff by ID
def show(id: int, db: Session):
    staff = db.query(models.Staff).filter(models.Staff.id == id).first()
    if not staff:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Staff with ID {id} not found")
    return staff
