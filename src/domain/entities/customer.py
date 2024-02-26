from pydantic import BaseModel, ConfigDict


class Customer(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int = None
    name: str
    email: str
    phone_number: str
