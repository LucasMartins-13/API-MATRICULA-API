from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.database as database, app.models as models, app.schemas as schemas

router = APIRouter()

@router.post("/", response_model=schemas.Aluno)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(database.get_db)):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.email == aluno.email).first()
    if db_aluno:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    
    novo_aluno = models.Aluno(nome=aluno.nome, email=aluno.email)
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno