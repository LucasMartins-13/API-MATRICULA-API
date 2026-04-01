# 🎓 Sistema de Matrícula Escolar API

API robusta para gerenciamento de alunos, cursos e matrículas, com regras de negócio integradas e validação automática.

## 🚀 Link da Aplicação
- **API Online:** [LINK_DO_RENDER_AQUI]
- **Documentação Swagger:** [LINK_DO_RENDER_AQUI/docs]

## 🛠️ Tecnologias Utilizadas
- FastAPI (Framework)
- SQLAlchemy (ORM)
- SQLite (Banco de dados)
- Pydantic (Validação de dados)

## ⚙️ Como rodar localmente
1. Clone o repositório:
   `git clone [LINK_DO_SEU_GITHUB]`
2. Crie e ative a venv:
   `python -m venv Venv` e `.\Venv\Scripts\activate`
3. Instale as dependências:
   `pip install -r requirements.txt`
4. Rode o servidor:
   `uvicorn main:app --reload`

## 📌 Principais Endpoints
- `POST /alunos/` - Cadastro de alunos
- `POST /matriculas/` - Matrícula (Limite de 5 por aluno)
- `PATCH /matriculas/{id}/concluir` - Finaliza um curso

## ☁️ Deploy (Instruções)
O projeto foi hospedado no **Render.com**.
1. Conecte o GitHub ao Render.
2. Comando de Build: `pip install -r requirements.txt`
3. Comando de Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`