from pydantic import BaseModel
from typing import Optional
from datetime import date

class Instructor(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True

class Course(BaseModel):
    id: Optional[int]
    title: str
    start_date: date
    max_size: int
    instructor_id: int

    class Config:
        orm_mode = True

class Lead(BaseModel):
    id: Optional[int]
    name: str
    email: str
    status: str

    class Config:
        orm_mode = True

class Comment(BaseModel):
    id: Optional[int]
    content: str
    course_id: int

    class Config:
        orm_mode = True


