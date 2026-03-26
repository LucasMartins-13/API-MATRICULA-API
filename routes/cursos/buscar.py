from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database, models, schemas

router = APIRouter()

@router.get("/{curso_id}", response_model=schemas.Curso)
def buscar_curso(curso_id: int, db: Session = Depends(database.get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso