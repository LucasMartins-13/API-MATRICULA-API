from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.database as database, app.models as models, app.schemas as schemas

router = APIRouter()

@router.get("/{aluno_id}", response_model=schemas.Aluno)
def buscar_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno