from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    
    #colocar matricula no aluno -- 




    #atalho????
    #atalho????
    #atalho????

    matriculas = relationship("Matricula", back_populates="aluno")

class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    
    #atalho????
    matriculas = relationship("Matricula", back_populates="curso")

class Matricula(Base):
    __tablename__ = "matriculas"
    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    
    # NOVO CAMPO: Padrão é "ativa"
    status = Column(String, default="ativa", nullable=False) 

    aluno = relationship("Aluno", back_populates="matriculas")
    curso = relationship("Curso", back_populates="matriculas")