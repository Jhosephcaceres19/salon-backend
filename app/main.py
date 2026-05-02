from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

from app.modules.users.controller import router as users
from app.modules.commissions.controller import router as commissions
from app.modules.jobs.controller import router as jobs
from app.modules.payments.controller import router as payments
from app.modules.services.controller import router as services
# importa los demás igual

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users)
app.include_router(commissions)
app.include_router(jobs)
app.include_router(payments)
app.include_router(services)