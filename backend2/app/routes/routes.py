from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from app.schemas.schemas import Charges
from app.services.service import ChargeService
from sqlalchemy.orm import Session
from app.config.db import get_db

charge = APIRouter()

@charge.get("/")
def read_root():
    response = RedirectResponse(url='http://localhost:8080')
    return response

@charge.post("/charges", status_code=status.HTTP_201_CREATED)
async def create_charge(charge: Charges, db: Session = Depends(get_db)):
    new_charge = ChargeService.create(db, charge)
    return JSONResponse(status_code=status.HTTP_201_CREATED, 
                        content={"message": "Charge created successfully", "charge": new_charge})