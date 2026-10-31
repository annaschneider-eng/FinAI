
from sqlalchemy import Column, Integer, String, Float, Date
from app.database.connection import Base


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    description = Column(String(255), nullable=False)

    amount = Column(Float, nullable=False)

    transaction_type = Column(String(20), nullable=False)

    category = Column(String(100), nullable=False)

    date = Column(Date, nullable=False)
