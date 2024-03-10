from fastapi import FastAPI, HTTPException, Depends
from models import Course as ModelCourse, Instructor as ModelInstructor, Lead, Comment
from schema import Course as SchemaCourse, Instructor as SchemaInstructor, Lead as SchemaLead, Comment as SchemaComment
from fastapi_sqlalchemy import DBSessionMiddleware,db
import os
from dotenv import load_dotenv
import uvicorn
from typing import List

load_dotenv(".env")
app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
@app.get("/")
async def root():
    return {"Message": "Hello world"}

@app.post("/add-instructor/", response_model=SchemaInstructor)
def add_instructor(instructor: SchemaInstructor):
    db_instructor = ModelInstructor(name=instructor.name)
    db.session.add(db_instructor)
    db.session.commit()
    db.session.refresh(db_instructor)
    return db_instructor

@app.post("/add-course/", response_model=SchemaCourse)
def add_course(course: SchemaCourse):
    db_instructor = db.session.query(ModelInstructor).filter(ModelInstructor.id == course.instructor_id).first()
    if not db_instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    db_course = ModelCourse(title=course.title, start_date=course.start_date, max_size=course.max_size, instructor=db_instructor)
    db.session.add(db_course)
    db.session.commit()
    db.session.refresh(db_course)
    return db_course

@app.put("/update-course/{course_id}/", response_model=SchemaCourse)
def update_course(course_id: int, updated_course: SchemaCourse):
    db_course = db.session.query(ModelCourse).filter(ModelCourse.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    db_course.title = updated_course.title
    db_course.start_date = updated_course.start_date
    db_course.max_size = updated_course.max_size
    db_instructor = db.session.query(ModelInstructor).filter(ModelInstructor.id == updated_course.instructor_id).first()
    if not db_instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    db_course.instructor = db_instructor
    db.session.commit()
    db.session.refresh(db_course)
    return db_course

@app.post("/register-course/{course_id}/", response_model=SchemaLead)
def register_course(course_id: int, lead: SchemaLead):
    db_course = db.session.query(ModelCourse).filter(ModelCourse.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    db_lead = Lead(name=lead.name, email=lead.email, status=lead.status)
    db_course.leads.append(db_lead)
    db.session.commit()
    db.session.refresh(db_lead)
    return db_lead

@app.put("/update-lead/{lead_id}/", response_model=SchemaLead)
def update_lead(lead_id: int, updated_lead: SchemaLead):
    db_lead = db.session.query(Lead).filter(Lead.id == lead_id).first()
    if not db_lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    db_lead.status = updated_lead.status
    db.session.commit()
    db.session.refresh(db_lead)
    return db_lead

@app.get("/search-leads/", response_model=List[SchemaLead])
def search_leads(query: str):
    leads = db.session.query(Lead).filter(Lead.name.ilike(f"%{query}%") | Lead.email.ilike(f"%{query}%")).all()
    return leads

@app.post("/add-comment/", response_model=SchemaComment)
def add_comment(comment: SchemaComment):
    db_course = db.session.query(ModelCourse).filter(ModelCourse.id == comment.course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    db_comment = Comment(content=comment.content,course_id=comment.course_id)
    db.session.add(db_comment)
    db.session.commit()
    db.session.refresh(db_comment)
    return db_comment
