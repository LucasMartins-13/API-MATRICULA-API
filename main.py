from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
from typing import List
from routes.cursos import criar, listar, buscar, atualizar, deletar

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Sistema de Matrículas")

app.include_router(criar.router, prefix="/cursos", tags=["Cursos"])
app.include_router(listar.router, prefix="/cursos", tags=["Cursos"])
app.include_router(buscar.router, prefix="/cursos", tags=["Cursos"])
app.include_router(atualizar.router, prefix="/cursos", tags=["Cursos"])
app.include_router(deletar.router, prefix="/cursos", tags=["Cursos"])

# Rota: Criar Aluno (POST)
@app.post("/alunos/", response_model=schemas.Aluno)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(database.get_db)):
    # Regra de Negócio: Verificar se o e-mail já existe
    db_aluno = db.query(models.Aluno).filter(models.Aluno.email == aluno.email).first()
    if db_aluno:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    
    novo_aluno = models.Aluno(nome=aluno.nome, email=aluno.email)
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno

# Rota: Listar Todos os Alunos (GET)
@app.get("/alunos/", response_model=List[schemas.Aluno])
def listar_alunos(db: Session = Depends(database.get_db)):
    return db.query(models.Aluno).all()

# Rota: Buscar Aluno por ID (GET)
@app.get("/alunos/{aluno_id}", response_model=schemas.Aluno)
def buscar_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

# Rota: Deletar Aluno (DELETE)
@app.delete("/alunos/{aluno_id}")
def deletar_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    db.delete(aluno)
    db.commit()
    return {"detail": "Aluno deletado com sucesso"}

@app.put("/alunos/{aluno_id}", response_model=schemas.Aluno)
def atualizar_aluno(aluno_id: int, aluno_dados: schemas.AlunoUpdate, db: Session = Depends(database.get_db)):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    # Atualiza apenas os campos que foram enviados
    if aluno_dados.nome:
        db_aluno.nome = aluno_dados.nome
    if aluno_dados.email:
        # Opcional: Validar se o novo email já existe em outro aluno
        db_aluno.email = aluno_dados.email

    db.commit()
    db.refresh(db_aluno)
    return db_aluno

# --- CRUD DE CURSOS ---

@app.post("/cursos/", response_model=schemas.Curso)
def criar_curso(curso: schemas.CursoCreate, db: Session = Depends(database.get_db)):
    novo_curso = models.Curso(titulo=curso.titulo)
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)
    return novo_curso

@app.get("/cursos/", response_model=list[schemas.Curso])
def listar_cursos(db: Session = Depends(database.get_db)):
    return db.query(models.Curso).all()

@app.get("/cursos/{curso_id}", response_model=schemas.Curso)
def buscar_curso(curso_id: int, db: Session = Depends(database.get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

@app.put("/cursos/{curso_id}", response_model=schemas.Curso)
def atualizar_curso(curso_id: int, curso_dados: schemas.CursoUpdate, db: Session = Depends(database.get_db)):
    db_curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not db_curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    if curso_dados.titulo:
        db_curso.titulo = curso_dados.titulo

    db.commit()
    db.refresh(db_curso)
    return db_curso

@app.delete("/cursos/{curso_id}")
def deletar_curso(curso_id: int, db: Session = Depends(database.get_db)):
    db_curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not db_curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    db.delete(db_curso)
    db.commit()
    return {"detail": "Curso deletado com sucesso"}

@app.post("/matriculas/", response_model=schemas.Matricula)
def matricular_aluno(matricula: schemas.MatriculaCreate, db: Session = Depends(database.get_db)):
    # 1. Validar se o aluno existe
    aluno = db.query(models.Aluno).filter(models.Aluno.id == matricula.aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno inexistente")

    # 2. Validar se o curso existe
    curso = db.query(models.Curso).filter(models.Curso.id == matricula.curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso inexistente")

    # 3. REGRA: Um aluno não pode se matricular duas vezes no mesmo curso
    duplicada = db.query(models.Matricula).filter(
        models.Matricula.aluno_id == matricula.aluno_id,
        models.Matricula.curso_id == matricula.curso_id
    ).first()
    
    if duplicada:
        raise HTTPException(status_code=400, detail="Aluno já matriculado neste curso")

    # 4. REGRA: No máximo 5 matrículas ATIVAS
    matriculas_ativas = db.query(models.Matricula).filter(
        models.Matricula.aluno_id == matricula.aluno_id,
        models.Matricula.status == "ativa"
    ).count()
    
    if matriculas_ativas >= 5:
        raise HTTPException(status_code=400, detail="Limite de 5 matrículas ativas atingido")

    # 5. Criar a matrícula com status padrão "ativa"
    nova_matricula = models.Matricula(
        aluno_id=matricula.aluno_id, 
        curso_id=matricula.curso_id,
        status="ativa"
    )
    db.add(nova_matricula)
    db.commit()
    db.refresh(nova_matricula)
    return nova_matricula

# Listar todos os cursos de um aluno
@app.get("/alunos/{aluno_id}/cursos")
def listar_cursos_do_aluno(aluno_id: int, db: Session = Depends(database.get_db)):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    # Extraímos os cursos das matrículas do aluno
    cursos = [m.curso for m in aluno.matriculas]
    return {"aluno": aluno.nome, "cursos": cursos}

# Listar todos os alunos de um curso
@app.get("/cursos/{curso_id}/alunos")
def listar_alunos_do_curso(curso_id: int, db: Session = Depends(database.get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    alunos = [m.aluno for m in curso.matriculas]
    return {"curso": curso.titulo, "alunos": alunos}