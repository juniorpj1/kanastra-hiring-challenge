from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.schemas import Charges
from app.models.models import ChargesModel

class ChargeService:
    @staticmethod
    def create(db: Session, charge: Charges):
        db_charge = ChargesModel(**charge.dict())
        try:
            db.add(db_charge)
            db.commit()
            db.refresh(db_charge)
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=str(e))
        
        # Convert the SQLAlchemy model instance to a Pydantic model
        return Charges.from_orm(db_charge)
