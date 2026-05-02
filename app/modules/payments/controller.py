from fastapi import APIRouter, Depends
from app.db.session import get_db
from app.models.pyments import Payment
from app.models.commissions import Commission
from app.models.jobs import Job

router = APIRouter()

@router.post("/{user_id}")
def pay(user_id: int, db=Depends(get_db)):
    commissions = db.query(Commission).join(Job)\
        .filter(Job.user_id == user_id, Commission.is_paid == False).all()

    total = sum(c.amount_paid for c in commissions)

    payment = Payment(user_id=user_id, total_paid=total)
    db.add(payment)

    for c in commissions:
        c.is_paid = True  # 🔥 CLAVE

    db.commit()

    return payment