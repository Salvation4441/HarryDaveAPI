from typing import Union

from fastapi import Depends, status, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import database, models, jwt_token
from hashing import Hash

# create an instance of the fastapi
router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)

#database connection
conn = database.connection


# auth user
# def authenticate_user(db: Session, username: str, password: str) -> Union[models.Customers, models.Staff, None]:
#     user = db.query(models.Staff).filter(models.Staff.email == username).first()
#     if user and Hash.verify(user.password, password):
#         return user
#
#     user = db.query(models.Customers).filter(models.Customers.email == username).first()
#     if user and Hash.verify(user.password, password):
#         return user
#
#     return None


# signin
@router.post('/')
# def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(conn)):
#     user = db.query(models.Staff).filter(models.Staff.email == request.username).first()
#     # user = authenticate_user(db, request.username, request.password)
#     user_count = db.query(models.Staff).count() + db.query(models.Customers).count()
#     if user_count < 1:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="No user in the database"
#         )
#
#     # if user is not logged in
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Invalid credentials")
#     # if password is incorrect
#     if not Hash.verify(user.password, request.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Invalid credentials")
#     # generate TOKEN
#
#     access_token = jwt_token.create_access_token(data={"sub": user.email})
#     return {'access_token': access_token, 'token_type': 'bearer'}
@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(conn)):
    # Check if the user is a staff member
    user = db.query(models.Staff).filter(models.Staff.email == request.username).first()
    user_role = 'staff'

    # If no staff found, check if the user is a customer
    if not user:
        user = db.query(models.Customers).filter(models.Customers.email == request.username).first()
        user_role = 'customer'

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )

    # Verify the password
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )

    # Generate the token with user role information
    access_token = jwt_token.create_access_token(data={"sub": user.email, "role": user_role})
    return {'access_token': access_token, 'token_type': 'bearer'}