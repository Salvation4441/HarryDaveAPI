from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel
import datetime


# Category Schema (for nested category relationship)
########################################################
class Category(BaseModel):
    name: str
    createdAt: datetime.datetime
    updatedAt: datetime.datetime

    class Config:
        orm_mode = True


# order details
#########################################################################
class OrderDetailBase(BaseModel):
    quantity: int
    price: float
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    product_id: int

    class Config:
        orm_mode = True


#########################################################################

# payment
###########################################################################
class PaymentBase(BaseModel):
    payment_date: datetime.datetime
    payment_method: str
    amount: float
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class Payment(PaymentBase):
    order_id: int

    class Config:
        orm_mode = True


######################################################################

# order Staff
######################################################################
class OrderStaffBase(BaseModel):
    shipped_date: Optional[datetime.datetime] = None
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class OrderStaff(OrderStaffBase):
    order_id: int

    class Config:
        orm_mode = True


##########################################################################


# delivery
##########################################################################
class DeliveryBase(BaseModel):
    order_id: int
    staff_id: int
    delivery_status: str
    customer_id: int


class Delivery(DeliveryBase):
    delivery_id: int
    createdAt: datetime.datetime
    updatedAt: datetime.datetime

    class Config:
        orm_mode = True
        # arbitrary_types_allowed = True


# Staff
######################################################################
class StaffBase(BaseModel):
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class Staff(StaffBase):
    firstname: str
    lastname: str
    phone: str
    email: str
    password: str
    role: str
    card_number: str
    order_staffs: List[OrderStaff] = []
    delivery: List[Delivery] = []

    class Config:
        orm_mode = True


##########################################################################


# orders
#########################################################################
class OrdersBase(BaseModel):
    order_date: datetime.datetime
    delivery_address: Optional[str] = None
    order_status: str
    total_amount: float
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class Order(OrdersBase):
    id: int
    # customer: Customers  # Replace with actual customer schema import
    order_details: List[OrderDetail] = []  # Replace with actual order detail schema import
    payment: Optional[Payment] = None  # Replace with actual payment schema import
    order_staffs: List[OrderStaff] = []  # Replace with actual order Staff schema import
    deliveries: List[Delivery] = []  # Replace with actual delivery schema import

    class Config:
        orm_mode = True


##################################################################################


#######################################################################
class CustomersBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    phone_number: str
    address: str
    city: str
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class Customers(CustomersBase):
    orders: List[Order] = []
    password:str

    class Config:
        orm_mode = True


class ShowCustomers(BaseModel):
    firstname: str
    lastname: str
    email: str
    phone_number: str
    address: str
    city: str

    # customers: List[Customers] = []  # Note the plural name 'customers'

    class Config:
        orm_mode = True


######################################################################

# products
#####################################################################
class ProductsBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    createdAt: datetime.datetime
    updatedAt: datetime.datetime


class Products(ProductsBase):
    class Config:
        orm_mode = True


# authentication
#####################################################################
class SignIn(BaseModel):
    email: str
    password: str
    role: str


####################################################################


####################################################################
# from the token generation
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    email: str
    role: List[str] = []
#####################################################################
