from pydantic import BaseModel

class UserRegister(BaseModel):
    name: str
    email: str
    password: str
    number: str

class AdminRegister(UserRegister):
    passkey: str  # required for admin registration

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str
    role: str
