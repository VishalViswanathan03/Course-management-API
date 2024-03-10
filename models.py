from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Instructor(Base):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    courses = relationship("Course", back_populates="instructor")

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    start_date = Column(Date)
    max_size = Column(Integer)
    instructor_id = Column(Integer, ForeignKey("instructors.id"))
    instructor = relationship("Instructor", back_populates="courses")
    leads = relationship("Lead", back_populates="course")

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    status = Column(String)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="leads")

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    course_id=Column(Integer,ForeignKey("courses.id"))

