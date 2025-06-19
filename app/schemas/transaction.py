from pydantic import BaseModel, EmailStr
from datetime import date

# --- Client ---

class ClientBase(BaseModel):
    name: str
    email: EmailStr

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    model_config = {
        "from_attributes": True
    }

# --- Project ---

class ProjectBase(BaseModel):
    name: str
    budget: float
    client_id: int

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    model_config = {
        "from_attributes": True
    }

# --- Payment ---

class PaymentBase(BaseModel):
    amount: float
    date: date
    project_id: int

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    model_config = {
        "from_attributes": True
    }

