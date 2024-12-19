from pydantic import BaseModel, Field
from typing import Optional

class AddressSchema(BaseModel):
    city: str
    country: str

class StudentSchema(BaseModel):
    name: str
    age: int
    address: AddressSchema

class UpdateStudentSchema(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[AddressSchema]
