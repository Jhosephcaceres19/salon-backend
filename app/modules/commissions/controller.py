from fastapi import APIRouter, Depends
from app.db.session import get_db
from app.models.commissions import Commission
from app.models.jobs import Job

router = APIRouter()

@router.post("/")
def create_commission(data: dict, db=Depends(get_db)):
    job = db.query(Job).get(data["job_id"])
    amount = job.price * (data["percentage"] / 100)

    c = Commission(
        job_id=data["job_id"],
        percentage=data["percentage"],
        amount_paid=amount
    )
    db.add(c)
    db.commit()
    return c