from sqlalchemy import Column, Integer, String
from databases import database

class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    number = Column(String, nullable=False)
    role = Column(String, nullable=False)  # 'admin' or 'user'
