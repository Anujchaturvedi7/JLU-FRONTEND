from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#sample_link
"""
DATABASE_URL = "postgresql://postgres:your_password@localhost/your_db"
"""
DATABASE_URL =  "postgresql://postgres:Anuj@localhost:5432/JLU"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
