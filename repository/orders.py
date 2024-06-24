from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

import models
import schemas


# get all Orders
def get_all(db: Session):
    order = db.query(models.Order).all()
    return order


def create(request: schemas.Order, db: Session,):
    order = models.Order(
        order_date=request.order_date,
        delivery_address=request.delivery_address,
        order_status=request.order_status,
        total_amount=request.total_amount,
        customer= request.customer.id,
        order_details=request.order_details,
        payment=request.payment.id,
        order_riders=request.order_riders,
        deliveries=request.deliveries
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    # return Order
    return {"message": "Order created successfully"}


# delete a product
# def delete(id: int, db: Session):
#     order = db.query(models.Order).filter(models.Order.id == id)
#     if not order.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail="Order not found")
#     order.delete(synchronize_session=False)
#     db.commit()
#     return {"message": "Order deleted successfully"}


# update order
def update(id: int, request: schemas.Order, db: Session):
    order = db.query(models.Order).filter(models.Order.id == id)
    if not order.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Order not found")
    order.update(dict(request), synchronize_session=False)
    db.commit()
    return {"message": "Order updated successfully"}


# get a Order by ID
def show(id: int, db: Session):
    order = db.query(models.Order).filter(models.Order.id == id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Order not found")
    return order
