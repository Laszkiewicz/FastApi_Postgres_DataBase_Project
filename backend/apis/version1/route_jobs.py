from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import create_new_job, retrieve_job

router = APIRouter()


@router.post("/create-job", response_model=ShowJob)
def create_job(job: JobCreate,db:Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job, db=db, owner_id=current_user)
    return job

@router.get("/get{id}", response_model=ShowJob)
def read_job(id:int, db:Session = Depends(get_db)):
    job = retrieve_job(id=id,db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with this id {id} does not exist")
    return job