from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import app.database as database, app.models as models, app.schemas as schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Aluno])
def listar_alunos(db: Session = Depends(database.get_db)):
    return db.query(models.Aluno).all()