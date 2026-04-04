from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
import app.database as database
import app.models as models
import app.schemas as schemas
from app.services import matricula_service

router = APIRouter()

@router.patch("/{matricula_id}/cancelar", response_model=schemas.Matricula)
def cancelar_matricula(matricula_id: int, db: Session = Depends(database.get_db)):
    mat = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()
    if not mat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Matrícula não encontrada")
    
    mat.status = "cancelada"
    db.commit()
    db.refresh(mat)
    return mat