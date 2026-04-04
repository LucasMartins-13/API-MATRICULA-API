from sqlalchemy.orm import Session
import app.models as models

def salvar_matricula(db: Session, matricula_dados):
    nova_matricula = models.Matricula(
        aluno_id=matricula_dados.aluno_id,
        curso_id=matricula_dados.curso_id,
        status="ativa"
    )
    db.add(nova_matricula)
    db.commit()
    db.refresh(nova_matricula)
    return nova_matricula