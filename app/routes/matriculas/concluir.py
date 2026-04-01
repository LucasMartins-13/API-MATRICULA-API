from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import app.database as database, app.models as models, app.schemas as schemas

router = APIRouter()

@router.patch("/{matricula_id}/concluir", response_model=schemas.Matricula)
def concluir_curso(matricula_id: int, db: Session = Depends(database.get_db)):
    mat = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()
    if not mat:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada")
    
    mat.status = "concluida"
    db.commit()
    db.refresh(mat)
    return mat