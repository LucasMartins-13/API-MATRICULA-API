from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from typing import List, Optional
import app.database as database, app.models as models, app.schemas as schemas

router = APIRouter()

@router.put("/{curso_id}", response_model=schemas.Curso)
def atualizar_curso(
    curso_id: int, 
    titulo: Optional[str] = Form(None), 
    db: Session = Depends(database.get_db)
):
    db_curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not db_curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    
    if titulo:
        db_curso.titulo = titulo

    db.commit()
    db.refresh(db_curso)
    return db_curso