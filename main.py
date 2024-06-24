from fastapi import FastAPI
from database import engine
import models
from routes import customers, products, orders, category, staff

app = FastAPI()

# connecting your model
models.Base.metadata.create_all(engine)

# get routes
app.include_router(customers.router)
app.include_router(products.router)
app.include_router(category.router)
app.include_router(orders.router)
app.include_router(staff.router)
