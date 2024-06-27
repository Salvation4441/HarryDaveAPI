from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

import models
from models import Customers, Order
import schemas


# get all Customers
def get_all(db: Session):
    customers = db.query(models.Customers).all()
    return customers


# create Customers
def create(request: schemas.Customers, db: Session):
    customers = models.Customers(
        firstname=request.firstname,
        lastname=request.lastname,
        email=request.email,
        phone_number=request.phone_number,
        address=request.address,
        city=request.city,
        orders=request.orders,
        createdAt = request.createdAt,
        updatedAt = request.updatedAt
    )
    if request.orders:
        customers.orders = [
            Order(
                order_date=order.order_date,
                delivery_address=order.delivery_address,
                order_status=order.order_status,
                total_amount=order.total_amount,
                customer_id=None  # This will be set automatically via the relationship
            ) for order in request.orders
        ]

    db.add(customers)
    db.commit()
    db.refresh(customers)
    # return customers
    return {"message": "Customers created successfully"}


# delete a Customers
# def delete(id: int, db: Session):
#     customers = db.query(models.Customers).filter(models.Customers.id == id)
#     if not customers.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Customers with ID {id} not found")
#     customers.delete(synchronize_session=False)
#     db.commit()
#     return f"Customers {id} deleted successfully"


# update a Customers
def update(id: int, request: schemas.Customers, db: Session):
    customers = db.query(models.Customers).filter(models.Customers.id == id)
    if not customers.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Customers not found")
    customers.update(dict(request), synchronize_session=False)
    db.commit()
    return {"message": "Customers updated successfully"}


def show(id: int, db: Session):
    customer = db.query(models.Customers).filter(models.Customers.id == id).first()  # get the first id
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'item {id} is not available')
    return customer
