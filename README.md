#  API de Matrícula Escolar

API desenvolvida com **FastAPI** e **SQLAlchemy** para gerenciamento de alunos, cursos e matrículas.

## Tecnologias
* Python 3.12+
* FastAPI
* SQLAlchemy (ORM)
* SQLite (Banco de Dados)

## Como rodar o projeto
1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv venv`.
3. Ative a venv: `.\venv\Scripts\activate` (Windows).
4. Instale as dependências: `pip install -r requirements.txt`.
5. Inicie o servidor: `uvicorn app.main:app --reload`.

## Principais Endpoints
* `GET /docs`: Documentação interativa.
* `POST /alunos/`: Cadastro de alunos.
* `POST /cursos/`: Cadastro de cursos.
* `POST /matriculas/`: Matricula um aluno em um curso.

## Regras da API
- Não é permitido cadastrar o mesmo e-mail para alunos diferentes.
- Não é permitido matricular um aluno duas vezes no mesmo curso.
- Validação de existência de IDs antes de efetivar a matrícula.