from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from app.core.config import SECRET_KEY, ALGORITHM

pwd = CryptContext(schemes=["bcrypt"])

def hash_password(p):
    return pwd.hash(p)

def verify(p, h):
    return pwd.verify(p, h)

def create_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(hours=8)

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)