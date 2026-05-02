from app.models.users import User
from app.core.security import hash_password, verify, create_token

def create_user(db, data):
    user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        role=data.role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login(db, data):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify(data.password, user.password):
        return None
    return create_token({"user_id": user.id, "role": user.role})