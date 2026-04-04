from fastapi import APIRouter, Depends, HTTPException, status, Form
from typing import List, Optional
from sqlalchemy.orm import Session
import app.database as database, app.models as models, app.schemas as schemas

router = APIRouter()

@router.put("/{aluno_id}", response_model=schemas.Aluno)
def atualizar_aluno(
    aluno_id: int, 
    nome: Optional[str] = Form(None), 
    email: Optional[str] = Form(None), 
    db: Session = Depends(database.get_db)
):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not db_aluno:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")
    
    if nome:
        db_aluno.nome = nome
    if email:
        db_aluno.email = email

    db.commit()
    db.refresh(db_aluno)
    return db_aluno