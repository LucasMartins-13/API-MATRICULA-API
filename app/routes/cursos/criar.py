from fastapi import APIRouter, Depends, status, Form
from sqlalchemy.orm import Session
import app.database as database, app.models as models, app.schemas as schemas

router = APIRouter()

@router.post("/", response_model=schemas.Curso, status_code=status.HTTP_201_CREATED)
def criar_curso(
    titulo: str = Form(...), 
    db: Session = Depends(database.get_db)
):
    novo_curso = models.Curso(titulo=titulo)
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)
    return novo_curso