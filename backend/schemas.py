from pydantic import BaseModel, ConfigDict, Field, ValidationError
import datetime
from typing import Literal

state = Literal["Applied", "Interview", "Offer", "Saved", "Rejected"] 
class ApplicationBase(BaseModel):

    company: str = Field(max_length=100)                            #Required
    role: str = Field( max_length=100)                              #Required
    link: str | None =Field(default=None, max_length=500)   
    job_board: str | None = Field(default=None, max_length=100)
    status: state = "Saved"                                         #default
    date_applied: datetime.date | None = None
    notes: str |  None = Field(default=None, max_length=1000)
    
class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    
    company: str = Field(default=None, max_length=100)              #Required
    role: str = Field(default=None, max_length=100)                 #Required
    link: str | None =Field(default=None, max_length=500)   
    job_board: str | None = Field(default=None, max_length=100)
    status: state | None = None
    date_applied: datetime.date | None = None
    notes: str |  None = Field(default=None, max_length=1000)


class ApplicationRead(ApplicationBase):

    model_config = ConfigDict(from_attributes=True)
    id: int
    



