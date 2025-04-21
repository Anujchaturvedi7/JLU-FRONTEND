from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from databases import database
from models import loginmodel
from schemas import loginschema #,UserLogin, Token, UserRegister, AdminRegister
from auth import loginauth #,verify_password, get_password_hash, create_access_token

# router = APIRouter()
router = APIRouter(prefix="/register")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# # 🚀 Register User
# @router.post("/register/user")
# def register_user(user: loginschema.UserRegister, db: Session = Depends(get_db)):
#     existing_email = db.query(loginmodel.User).filter(loginmodel.User.email == user.email).first()
#     if existing_email:
#         raise HTTPException(status_code=400, detail="Email already exists")
#     existing_number = db.query(loginmodel.User).filter(loginmodel.User.number == user.number).first()
#     if existing_number:
#         raise HTTPException(status_code=400, detail="Number already exists")
    
#     hashed_pw = loginauth.get_password_hash(user.password)
#     new_user = loginmodel.User(
#         username=user.email,
#         password=hashed_pw,
#         name=user.name,
#         number=user.number,
#         role="user"
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {"message": "User registered successfully"}

# # 🚀 Register Admin
# @router.post("/register/admin")
# def register_admin(admin: loginschema.AdminRegister, db: Session = Depends(get_db)):
#     if admin.passkey != "1234":
#         raise HTTPException(status_code=401, detail="Invalid admin passkey")

#     existing = db.query(loginmodel.User).filter(loginmodel.User.username == admin.email).first()
#     if existing:
#         raise HTTPException(status_code=400, detail="Admin already exists")

#     hashed_pw = loginauth.get_password_hash(admin.password)
#     new_admin = loginmodel.User(
#         username=admin.email,
#         password=hashed_pw,
#         name=admin.name,
#         number=admin.number,
#         role="admin"
#     )
#     db.add(new_admin)
#     db.commit()
#     db.refresh(new_admin)
#     return {"message": "Admin registered successfully"}
@router.post("/user")
def register_user(user: loginschema.UserRegister, db: Session = Depends(get_db)):
    existing = db.query(loginmodel.User).filter(loginmodel.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    existing = db.query(loginmodel.User).filter(loginmodel.User.number == user.number).first()
    if existing:
        raise HTTPException(status_code=400, detail="Number already exists")
    
    hashed_pw = loginauth.get_password_hash(user.password)
    new_user = loginmodel.User(
        username=user.name,
        email = user.email,
        password=hashed_pw,
        name=user.name,
        number=user.number,
        role="user"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

@router.post("/admin")
def register_admin(admin: loginschema.AdminRegister, db: Session = Depends(get_db)):
    if admin.passkey != "1234":
        raise HTTPException(status_code=401, detail="Invalid admin passkey")

    existing = db.query(loginmodel.User).filter(loginmodel.User.email == admin.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    existing = db.query(loginmodel.User).filter(loginmodel.User.number == admin.number).first()
    if existing:
        raise HTTPException(status_code=400, detail="Number already exists")

    hashed_pw = loginauth.get_password_hash(admin.password)
    new_admin = loginmodel.User(
        username=admin.name,
        email = admin.email,
        password=hashed_pw,
        name=admin.name,
        number=admin.number,
        role="admin"
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return {"message": "Admin registered successfully"}
