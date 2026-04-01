from fastapi import HTTPException
from sqlalchemy.orm import Session
import app.models as models
from app.crud import matricula_crud

def realizar_matricula(db: Session, matricula_dados):
    #Validar Aluno e Curso
    aluno = db.query(models.Aluno).filter(models.Aluno.id == matricula_dados.aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno inexistente")

    curso = db.query(models.Curso).filter(models.Curso.id == matricula_dados.id).first() # Corrigido para curso_id se necessário
    if not curso:
        raise HTTPException(status_code=404, detail="Curso inexistente")

    #Validar Duplicada
    duplicada = db.query(models.Matricula).filter(
        models.Matricula.aluno_id == matricula_dados.aluno_id,
        models.Matricula.curso_id == matricula_dados.curso_id
    ).first()
    if duplicada:
        raise HTTPException(status_code=400, detail="Aluno já matriculado neste curso")

    #Validar Limite de 5
    ativas = db.query(models.Matricula).filter(
        models.Matricula.aluno_id == matricula_dados.aluno_id,
        models.Matricula.status == "ativa"
    ).count()
    if ativas >= 5:
        raise HTTPException(status_code=400, detail="Limite de 5 matrículas ativas atingido")

    return matricula_crud.salvar_matricula(db, matricula_dados)