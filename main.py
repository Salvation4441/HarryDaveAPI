from fastapi import FastAPI
from database import engine
import models
from routes import products, orders, category, staff, authentication, delivery,  customers

app = FastAPI()

# connecting your model
models.Base.metadata.create_all(engine)

# get routes
# authentication
app.include_router(authentication.router)
app.include_router(staff.router)
app.include_router(customers.router)
app.include_router(products.router)
app.include_router(category.router)
app.include_router(orders.router)
app.include_router(delivery.router)


