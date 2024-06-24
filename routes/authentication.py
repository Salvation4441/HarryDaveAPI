from fastapi import Depends, status, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, models, token
from ..hashing import Hash

# create an instance of the fastapi
router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)

#database connection
conn = database.connection


# signin
@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(conn)):
    user = db.query(models.Staff).filter(models.Staff.email == request.email).first()
    # if user is not logged in
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid credentials")
    # if password is incorrect
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid credentials")
    # generate TOKEN

    access_token = token.create_access_token(data={"sub": user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}
