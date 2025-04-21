from fastapi import FastAPI
from databases import database
from models.loginmodel import User
from routes import login, register
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

app.include_router(login.router)
app.include_router(register.router)


# Enable CORS for all origins (you can specify your frontend's URL instead of "*")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace '*' with your frontend's URL (e.g., ["http://localhost:5173"])
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)
