from fastapi import APIRouter, Depends, HTTPException, status, Form
from typing import List, Optional
from sqlalchemy.orm import Session
import app.database as database, app.models as models

router = APIRouter()

@router.get("/curso/{curso_id}/alunos")
def listar_alunos_do_curso(curso_id: int, db: Session = Depends(database.get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    
    alunos = [m.aluno for m in curso.matriculas]
    return {"curso": curso.titulo, "alunos": alunos}