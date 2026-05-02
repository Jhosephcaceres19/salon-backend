from fastapi import APIRouter, Depends
from app.db.session import get_db
from app.models.jobs import Job

router = APIRouter()

@router.post("/")
def create_job(data: dict, db=Depends(get_db)):
    job = Job(**data)
    db.add(job)
    db.commit()
    return job