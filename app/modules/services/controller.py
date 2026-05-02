from fastapi import APIRouter, Depends
from app.db.session import get_db
from app.models.services import Service

router = APIRouter()

@router.post("/")
def create_service(data: dict, db=Depends(get_db)):
    s = Service(**data)
    db.add(s)
    db.commit()
    return s