
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import date

from app.database.connection import get_db
from app.models.transaction import Transaction

router = APIRouter(
    prefix="/transactions",
    tags=["Transações"]
)


# Estrutura dos dados recebidos pela API
class TransactionCreate(BaseModel):
    description: str
    amount: float
    transaction_type: str
    category: str
    date: date


# Cadastrar uma transação
@router.post("/")
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    if transaction.transaction_type not in ["receita", "despesa"]:
        raise HTTPException(
            status_code=400,
            detail="Tipo deve ser receita ou despesa."
        )

    new_transaction = Transaction(
        description=transaction.description,
        amount=transaction.amount,
        transaction_type=transaction.transaction_type,
        category=transaction.category,
        date=transaction.date
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return new_transaction


# Consultar todas as transações
@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()
