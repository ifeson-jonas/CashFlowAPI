printf '%s\n' '
<h1 align="center">💸 CashFlowAPI</h1>
<p align="center">
  API RESTful para controle financeiro de clientes, projetos e pagamentos.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-0.110-green?logo=fastapi" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-blue" />
  <img src="https://img.shields.io/badge/Tested%20with-Pytest-yellow" />
</p>

---

## 🚀 Sobre o projeto

O **CashFlowAPI** é uma aplicação backend desenvolvida com FastAPI que permite:

- Cadastrar e listar clientes 👤
- Gerenciar projetos ligados a clientes 💼
- Registrar pagamentos por projeto 💰

Ideal para pequenos negócios que precisam de um sistema simples e eficiente de controle financeiro.

---

## 📦 Tecnologias usadas

- [x] Python 3.12  
- [x] FastAPI  
- [x] SQLAlchemy  
- [x] SQLite (pode migrar para PostgreSQL facilmente)  
- [x] Pydantic  
- [x] Uvicorn  
- [x] Pytest

---

## ⚙️ Como rodar o projeto

```bash
# Clone o repositório
git clone https://github.com/ifeson-jonas/CashFlowAPI.git
cd CashFlowAPI

# Crie o ambiente virtual
python3.12 -m venv venv
source venv/bin/activate.fish  # ou source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
uvicorn app.main:app --reload
