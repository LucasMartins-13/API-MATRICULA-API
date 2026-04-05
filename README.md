# 🎓 Sistema de Matrícula Escolar API

API robusta para gerenciamento de alunos, cursos e matrículas, com regras de negócio integradas e validação automática.

## 🚀 Link da Aplicação
- **API Online:** `https://api-matricula-e8ji.onrender.com`
- **Documentação Swagger:** `https://api-matricula-e8ji.onrender.com/docs`   (para acessar API, use esse link)

## 🛠️ Tecnologias Utilizadas
- FastAPI (Framework)
- SQLAlchemy (ORM)
- SQLite (Banco de dados)
- Pydantic (Validação de dados)

## ⚙️ Como rodar localmente
1. Clone o repositório:
   `git clone https://github.com/LucasMartins-13/API-MATRICULA-API`
2. Crie e ative a venv:
   `python -m venv Venv` e `.\Venv\Scripts\activate`
3. Instale as dependências:
   `pip install -r requirements.txt`
4. Rode o servidor:
   `uvicorn main:app --reload`
5. link URL
   `acesse o link do uvicorn e coloque um /docs no final`

## 📌 Principais Endpoints
- `POST /alunos/` - Cadastro de alunos
- `POST /matriculas/` - Matrícula (Limite de 5 por aluno)
- `PATCH /matriculas/{id}/concluir` - Finaliza um curso

## ☁️ Deploy (Instruções)
O projeto foi hospedado no **Render.com**.
1. GitHub conectado ao Render.
2. Comando de Build usado: `pip install -r requirements.txt`
3. Comando de Start usado: `uvicorn main:app --host 0.0.0.0 --port $PORT`
