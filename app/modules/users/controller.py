from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserLogin
from app.db.session import SessionLocal
from .service import create_user, login

router = APIRouter(prefix="/users")

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/register")
def register(data: UserCreate, db=Depends(get_db)):
    return create_user(db, data)

@router.post("/login")
def login_user(data: UserLogin, db=Depends(get_db)):
    token = login(db, data)
    if not token:
        return {"error": "invalid"}
    return {"access_token": token}