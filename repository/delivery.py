from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

import models
import schemas


# get all delivery
def get_all(db: Session):
    delivery = db.query(models.Delivery).all()
    return delivery


def create(request: schemas.Delivery, db: Session):
    delivery = models.Delivery(
        delivery_id = request.delivery_id,
        delivery_status = request.delivery_status,
        order_id = request.order_id,
        staff_id = request.staff_id,
        customer_id = request.customer_id,
        createdAt = request.createdAt,
        updatedAt = request.updatedAt
    )
    db.add(delivery)
    db.commit()
    db.refresh(delivery)
    # return delivery
    return {"message": "delivery created successfully"}


# delete a delivery
# def delete(id: int, db: Session):
#     delivery = db.query(models.delivery).filter(models.delivery.id == id)
#     if not delivery.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail="delivery not found")
#     delivery.delete(synchronize_session=False)
#     db.commit()
#     return {"message": "delivery deleted successfully"}


# update a delivery
def update(id: int, request: schemas.Delivery, db: Session):
    delivery = db.query(models.Delivery).filter(models.Delivery.id == id)
    if not delivery.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="delivery not found")
    delivery.update(dict(request), synchronize_session=False)
    db.commit()
    return {"message": "delivery updated successfully"}


# get a delivery by ID
def show(id: int, db: Session):
    delivery = db.query(models.Delivery).filter(models.Delivery.id == id).first()
    if not delivery:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="delivery not found")
    return delivery

