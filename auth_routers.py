from fastapi import APIRouter, HTTPException,status
from database import Session,engine,sessionmaker
from schemas import SignUpModel
from models import User
from werkzeug.security import generate_password_hash,check_password_hash


auth_router = APIRouter(
    prefix='/auth',
    tags=["Auth"]
)
session = Session(bind=engine)

@auth_router.get('/')
def hello():
    return {"detail":"Ismatov"}


@auth_router.post("/signup",status_code=status.HTTP_201_CREATED)
def signup(user:SignUpModel):
    db_email = session.query(User).filter(User.email==user.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="this email already exists")
    db_username = session.query(User).filter(User.username==user.username).first()
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="this username already exists")

    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_active=user.is_active,
        is_staff=user.is_staff
    )
    session.add(new_user)
    session.commit()
    return new_user