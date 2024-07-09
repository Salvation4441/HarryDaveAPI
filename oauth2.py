from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt_token
import models
from sqlalchemy.orm import Session
import database

# login route where the api will fetch token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
conn = database.connection


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(conn)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = jwt_token.verify_token(token, credentials_exception)

    if token_data.role == "staff":
        user = db.query(models.Staff).filter(models.Staff.email == token_data.email).first()
    else:
        user = db.query(models.Customers).filter(models.Customers.email == token_data.email).first()

    if user is None:
        raise credentials_exception

    return user, token_data.role

    # return jwt_token.verify_token(token, credentials_exception)
