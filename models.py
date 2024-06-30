from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime, func
from database import Base
from sqlalchemy.orm import relationship
from typing import Optional


# customer
class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)
    city = Column(String)
    password = Column(String)
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    orders = relationship('Order', back_populates='customers')
    delivery = relationship('Delivery', back_populates='customers')


# # category
class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())
    products = relationship('Products', back_populates='category')


# # product
class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Numeric(10, 2), nullable=False)
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='products')


# Order class
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime, nullable=False)
    delivery_address = Column(String(255))
    order_status = Column(String(50))
    total_amount = Column(Numeric(10, 2))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    customers = relationship('Customers', back_populates='orders')
    order_details = relationship('OrderDetail', back_populates='orders')
    payments = relationship('Payment', uselist=False, back_populates='orders')
    order_staff = relationship('OrderStaff', back_populates='orders')
    delivery = relationship('Delivery', back_populates='orders')



# OrderDetail class
class OrderDetail(Base):
    __tablename__ = 'order_details'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Numeric(10, 2))
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    orders = relationship('Order', back_populates='order_details')


# Payment class
class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    payment_date = Column(DateTime, nullable=False)
    payment_method = Column(String(50))
    amount = Column(Numeric(10, 2), nullable=False)
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    # staff_id should be here

    orders = relationship('Order', back_populates='payments')


# PaymentMethod class
class PaymentMethod(Base):
    __tablename__ = 'payment_methods'

    payment_method_id = Column(Integer, primary_key=True, index=True)
    payment_method_name = Column(String(50), nullable=False)
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())


# PaymentStatus class
class PaymentStatus(Base):
    __tablename__ = 'payment_status'

    payment_status_id = Column(Integer, primary_key=True, index=True)
    payment_status_name = Column(String(50), nullable=False)
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())


# Rider class
# change the riders to staff
class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    phone = Column(String)
    email = Column(String)
    role = Column(String(100), nullable=False)
    password = Column(String)
    card_number = Column(String)
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    order_staff = relationship('OrderStaff', back_populates='staff')
    delivery = relationship('Delivery', back_populates='staff')


# OrderStaff class
# change it to staff (tablename)
class OrderStaff(Base):
    __tablename__ = 'order_staff'

    id = Column(Integer, primary_key=True, index=True)
    shipped_date = Column(DateTime)
    order_id = Column(Integer, ForeignKey('orders.id'))
    staff_id = Column(Integer, ForeignKey('staff.id'))
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    orders = relationship('Order', back_populates='order_staff')
    staff = relationship('Staff', back_populates='order_staff')


# Delivery class
class Delivery(Base):
    __tablename__ = 'delivery'

    delivery_id = Column(Integer, primary_key=True, index=True)
    delivery_status = Column(String(100), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'))
    staff_id = Column(Integer, ForeignKey('staff.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    orders = relationship('Order', back_populates='delivery')
    staff = relationship('Staff', back_populates='delivery')
    customers = relationship('Customers', back_populates='delivery')


