from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ChargesModel(Base):
    __tablename__ = 'charges'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    governmentId = Column(String)
    email = Column(String)
    debtAmount = Column(Float)
    debtDueDate = Column(String)
