from fastapi import APIRouter
from app.api.routes import clients, projects, payments

router = APIRouter()

router.include_router(clients.router, prefix="/clients", tags=["Clients"])
router.include_router(projects.router, prefix="/projects", tags=["Projects"])
router.include_router(payments.router, prefix="/payments", tags=["Payments"])
