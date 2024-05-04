from pydantic import BaseModel

class Charges(BaseModel):
    name: str
    governmentId: str
    email: str
    debtAmount: float
    debtDueDate: str
    