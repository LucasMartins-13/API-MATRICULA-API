from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database, models, schemas

router = APIRouter()

@router.put("/{curso_id}", response_model=schemas.Curso)
def atualizar_curso(curso_id: int, curso_dados: schemas.CursoUpdate, db: Session = Depends(database.get_db)):
    db_curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not db_curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    if curso_dados.titulo:
        db_curso.titulo = curso_dados.titulo

    db.commit()
    db.refresh(db_curso)
    return db_curso