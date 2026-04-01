from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import app.models as models, app.database as database


# --- IMPORTAÇÃO DOS MODULOS ---

#Cursos
from app.routes.cursos import (
    criar as cc, 
    listar as lc, 
    buscar as bc, 
    atualizar as ac, 
    deletar as dc,

)

#Alunos
from app.routes.alunos import (
    criar as ca, 
    listar as la, 
    buscar as ba, 
    atualizar as aa, 
    deletar as da, 
    listar_cursos as lca
)

#Matriculas
from app.routes.matriculas import matricular, cancelar, concluir

#Tabela
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Sistema de Matrículas")

# --- (Sprint 3) ---
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "statusCode": exc.status_code
        }
    )

#ROTAS

#Cursos
app.include_router(cc.router, prefix="/cursos", tags=["Cursos"])
app.include_router(lc.router, prefix="/cursos", tags=["Cursos"])
app.include_router(bc.router, prefix="/cursos", tags=["Cursos"])
app.include_router(ac.router, prefix="/cursos", tags=["Cursos"])
app.include_router(dc.router, prefix="/cursos", tags=["Cursos"])

#Alunos
app.include_router(ca.router, prefix="/alunos", tags=["Alunos"])
app.include_router(la.router, prefix="/alunos", tags=["Alunos"])
app.include_router(ba.router, prefix="/alunos", tags=["Alunos"])
app.include_router(aa.router, prefix="/alunos", tags=["Alunos"])
app.include_router(da.router, prefix="/alunos", tags=["Alunos"])
app.include_router(lca.router, prefix="/alunos", tags=["Alunos"])

#Matriculas
app.include_router(matricular.router, prefix="/matriculas", tags=["Matrículas"])
app.include_router(cancelar.router, prefix="/matriculas", tags=["Matrículas"])
app.include_router(concluir.router, prefix="/matriculas", tags=["Matrículas"])