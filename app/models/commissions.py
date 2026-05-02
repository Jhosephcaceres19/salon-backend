from sqlalchemy import Column, Integer, Float, ForeignKey, Boolean, DateTime
from datetime import datetime
from app.db.base import Base

class Commission(Base):
    __tablename__ = "commissions"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    percentage = Column(Float)
    amount_paid = Column(Float)
    is_paid = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)