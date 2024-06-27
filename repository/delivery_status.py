from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

import models
import schemas


# get all DeliveryStatus
def get_all(db: Session):
    delivery_status = db.query(models.DeliveryStatus).all()
    return delivery_status


def create(request: schemas.DeliveryStatus, db: Session):
    delivery_status = models.DeliveryStatus(
        delivery_status = request.delivery_status,
        order_id = request.order_id,
        delivery_status_id = request.delivery_status_id,
        createdAt = request.createdAt,
        updatedAt = request.updatedAt
    )
    db.add(delivery_status)
    db.commit()
    db.refresh(delivery_status)
    # return DeliveryStatus
    return {"message": "DeliveryStatus created successfully"}


# delete a DeliveryStatus
# def delete(id: int, db: Session):
#     DeliveryStatus = db.query(models.DeliveryStatus).filter(models.DeliveryStatus.id == id)
#     if not DeliveryStatus.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail="DeliveryStatus not found")
#     DeliveryStatus.delete(synchronize_session=False)
#     db.commit()
#     return {"message": "DeliveryStatus deleted successfully"}


# update a DeliveryStatus
def update(id: int, request: schemas.DeliveryStatus, db: Session):
    delivery_status = db.query(models.DeliveryStatus).filter(models.DeliveryStatus.id == id)
    if not delivery_status.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="DeliveryStatus not found")
    delivery_status.update(dict(request), synchronize_session=False)
    db.commit()
    return {"message": "DeliveryStatus updated successfully"}


# get a DeliveryStatus by ID
def show(id: int, db: Session):
    delivery_status = db.query(models.DeliveryStatus).filter(models.DeliveryStatus.id == id).first()
    if not delivery_status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="DeliveryStatus not found")
    return delivery_status

