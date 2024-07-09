from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

import models
import schemas
from oauth2 import get_current_user


# get all Orders
def get_all(db: Session):
    order = db.query(models.Order).all()
    return order


def create(request: schemas.Order, db: Session,current_user: models.Customers = Depends(get_current_user)):
    # Get the currently logged-in customer
    customer = current_user
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")

    # Create the Order object
    order = models.Order(
        order_date=request.order_date,
        delivery_address=request.delivery_address,
        order_status=request.order_status,
        total_amount=request.total_amount,
        customer_id=customer.id
    )

    # Add OrderDetails if provided
    if request.order_details:
        order.order_details = [
            models.OrderDetail(
                product_id=detail.product_id,
                quantity=detail.quantity,
                price=detail.price
            ) for detail in request.order_details
        ]

    # Add Payment if provided
    if request.payment:
        order.payment = models.Payment(
            payment_date=request.payment.payment_date,
            payment_method=request.payment.payment_method,
            amount=request.payment.amount
        )

    # Add OrderStaff if provided
    if request.order_staffs:
        order.order_staff = [
            models.OrderStaff(
                staff_id=staff.staff_id,
                shipped_date=staff.shipped_date
            ) for staff in request.order_staffs
        ]

    # Add Deliveries if provided
    if request.deliveries:
        order.delivery = [
            models.Delivery(
                delivery_status=delivery.delivery_status,
                order_id=order.id,
                staff_id=delivery.staff_id,
                customer_id=delivery.customer_id
            ) for delivery in request.deliveries
        ]

    db.add(order)
    db.commit()
    db.refresh(order)
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
