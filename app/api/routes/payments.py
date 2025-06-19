from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Payment)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    db_project = db.query(models.Project).filter(models.Project.id == payment.project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    new_payment = models.Payment(amount=payment.amount, date=payment.date, project_id=payment.project_id)
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

@router.get("/", response_model=list[schemas.Payment])
def read_payments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Payment).offset(skip).limit(limit).all()
