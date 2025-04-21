# from database import SessionLocal
# from models import User
# from auth import get_password_hash

# def create_admin():
#     db = SessionLocal()
#     existing = db.query(User).filter(User.username == "admin").first()
#     if not existing:
#         user = User(username="admin", password=get_password_hash("admin123"), role="admin")
#         db.add(user)
#         db.commit()
#         print("Admin user created!")
#     else:
#         print("Admin user already exists.")

# create_admin()
