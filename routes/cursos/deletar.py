from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database, models, schemas

router = APIRouter()

@router.delete("/{curso_id}")
def deletar_curso(curso_id: int, db: Session = Depends(database.get_db)):
    db_curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not db_curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    db.delete(db_curso)
    db.commit()
    return {"detail": "Curso deletado com sucesso"}