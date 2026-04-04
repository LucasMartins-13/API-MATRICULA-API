from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
import app.database as database, app.models as models, app.schemas as schemas
from typing import List, Optional

router = APIRouter()

@router.post("/", response_model=schemas.Aluno, status_code=status.HTTP_201_CREATED)
def criar_aluno(
    nome: str = Form(...), 
    email: str = Form(...), 
    db: Session = Depends(database.get_db)
):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.email == email).first()
    if db_aluno:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="E-mail já cadastrado")
    
    novo_aluno = models.Aluno(nome=nome, email=email)
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno