from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from app.schemas.schemas import Charges
from app.services.service import ChargeService
from sqlalchemy.orm import Session
from app.config.db import get_db
from fastapi import Request

charge = APIRouter()

@charge.get("/")
def read_root(request: Request):
    # Verifica se a solicitação já veio de 'http://localhost:8080'
    if "localhost:8080" in str(request.url):
        return JSONResponse(content={"message": "Você já está na página inicial!"})
    else:
        response = RedirectResponse(url='http://localhost:8080')
        return response

@charge.post("/charges", status_code=status.HTTP_201_CREATED)
async def create_charge(charge: Charges, db: Session = Depends(get_db)):
        new_charge = ChargeService.create(db, charge)
        return JSONResponse(status_code=status.HTTP_201_CREATED, 
                            content={"message": "Charge created successfully", "charge": new_charge})
    