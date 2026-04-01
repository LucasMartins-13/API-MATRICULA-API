from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.database as database, app.models as models, app.schemas as schemas

router = APIRouter()

@router.put("/{aluno_id}", response_model=schemas.Aluno)
def atualizar_aluno(aluno_id: int, aluno_dados: schemas.AlunoUpdate, db: Session = Depends(database.get_db)):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    if aluno_dados.nome:
        db_aluno.nome = aluno_dados.nome
    if aluno_dados.email:
        db_aluno.email = aluno_dados.email

    db.commit()
    db.refresh(db_aluno)
    return db_aluno