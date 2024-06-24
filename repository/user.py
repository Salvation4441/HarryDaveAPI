from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..hashing import Hash


# create a Staff
def register(request: schemas.Staff, db: Session):
    # Check if the Staff already exists
    exiting_staff = db.query(models.Staff).filter(models.Staff.email == request.email).first()
    if exiting_staff:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Staff with this email already exists")
    # Create a new Staff
    new_staff = models.Staff(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return {f'message': 'Staff has been created successfully'}


# show Staff by id
def show_staff_by_id(id: int, db: Session):
    staff = db.query(models.Staff).filter(models.Staff.id == id).first()
    if not staff:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Staff with id {id} not found")
    return staff


# get all Staffs
def show_Staffs(db: Session):
    staffs = db.query(models.Staff).all()
    return staffs
