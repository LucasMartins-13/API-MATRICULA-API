from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# --- ALUNO ---
class AlunoCreate(BaseModel):
    nome: str = Field(..., min_length=1, description="Nome não pode ser vazio")
    email: EmailStr

class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None

class Aluno(BaseModel):
    id: int
    nome: str
    email: str
    class Config:
        from_attributes = True

# --- CURSO ---
class CursoCreate(BaseModel):
    titulo: str = Field(..., min_length=1, description="O título é obrigatório")

class CursoUpdate(BaseModel):
    titulo: Optional[str] = None

class Curso(BaseModel):
    id: int
    titulo: str
    class Config:
        from_attributes = True

# --- MATRICULAS ---
class MatriculaCreate(BaseModel):
    aluno_id: int
    curso_id: int

class Matricula(BaseModel):
    id: int
    aluno_id: int
    curso_id: int
    status: str #ativa, cancelada ou concluida

    class Config:
        from_attributes = True

class AlunoComCursos(Aluno):
    cursos: List[Curso] = []

class CursoComAlunos(Curso):
    alunos: List[Aluno] = []

    