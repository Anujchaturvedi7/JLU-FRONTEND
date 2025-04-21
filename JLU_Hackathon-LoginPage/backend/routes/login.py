from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from databases import database
from models import loginmodel
from schemas import loginschema
from auth import loginauth

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=loginschema.Token)
def login(user: loginschema.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(loginmodel.User).filter(loginmodel.User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    if not loginauth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = loginauth.create_access_token(data={"sub": db_user.email, "role": db_user.role})
    return {"access_token": access_token, "token_type": "bearer"}
