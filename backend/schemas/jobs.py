from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()
    company_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None


class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str


class ShowJob(JobBase):
    title: str
    company: str
    location: str
    date_posted: date
    description: Optional[str]

    class Config:
        orm_mode = True
