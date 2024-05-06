from pydantic import BaseModel

class Charges(BaseModel):
    name: str
    governmentId: str
    email: str
    debtAmount: float
    debtDueDate: str

    class Config:
        orm_mode = True
        from_attributes = True
