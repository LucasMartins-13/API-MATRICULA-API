from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import database, models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Curso, status_code=201)
def criar_curso(curso: schemas.CursoCreate, db: Session = Depends(database.get_db)):
    novo_curso = models.Curso(titulo=curso.titulo)
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)
    return novo_curso