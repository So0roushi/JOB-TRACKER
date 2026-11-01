from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import datetime
from sqlalchemy import Text
from backend.database import Base

#using sql alchemy to define the structure of the table, instead of hardcoding sql
class Application(Base):
    
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    company: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
    link: Mapped[Optional[str]] 
    job_board: Mapped[Optional[str]]
    status: Mapped[str] = mapped_column(default="Saved" ,nullable=False)
    date_applied: Mapped[Optional[datetime.date]]
    notes: Mapped[Optional[str]] = mapped_column(Text)


     

