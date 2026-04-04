from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
import app.database as database
import app.models as models
import app.schemas as schemas
from app.services import matricula_service

router = APIRouter()

@router.post("/", response_model=schemas.Matricula, status_code=status.HTTP_201_CREATED)
def matricular(
    aluno_id: int = Form(...),
    curso_id: int = Form(...),
    db: Session = Depends(database.get_db)
):
    nova_matricula = schemas.MatriculaCreate(aluno_id=aluno_id, curso_id=curso_id)
    return matricula_service.realizar_matricula(db, nova_matricula)