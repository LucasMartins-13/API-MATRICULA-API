from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session                   
import app.database as database, app.models as models, app.schemas as schemas
from app.services import matricula_service

router = APIRouter()

@router.post("/", response_model=schemas.Matricula)
def matricular(matricula: schemas.MatriculaCreate, db: Session = Depends(database.get_db)):
    #service
    return matricula_service.realizar_matricula(db, matricula)