from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# --- SCHEMAS DE ALUNO ---

class AlunoCreate(BaseModel):
    # Field(..., min_length=1) obriga que o campo não seja vazio ""
    nome: str = Field(..., min_length=1, description="Nome não pode ser vazio")
    email: EmailStr # Já valida se o formato é de e-mail (ex@ex.com)

class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None

class Aluno(BaseModel):
    id: int
    nome: str
    email: str
    class Config:
        from_attributes = True

    class Config:
        from_attributes = True


# --- SCHEMAS DE CURSO ---

class CursoCreate(BaseModel):
    titulo: str = Field(..., min_length=1, description="O título é obrigatório")

class CursoUpdate(BaseModel):
    titulo: Optional[str] = None

class Curso(BaseModel):
    id: int
    titulo: str
    class Config:
        from_attributes = True

# --- SCHEMAS DE MATRICULAS ---

class MatriculaCreate(BaseModel):
    aluno_id: int
    curso_id: int

class Matricula(BaseModel):
    id: int
    aluno_id: int
    curso_id: int
    status: str # "ativa", "cancelada" ou "concluida"

    class Config:
        from_attributes = True

class AlunoComCursos(Aluno):
    cursos: List[Curso] = []

class CursoComAlunos(Curso):
    alunos: List[Aluno] = []

    