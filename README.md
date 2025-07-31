# 🔍 MeSH Term Search App

This project provides a MeSH (Medical Subject Headings) term search tool using:
- 🚀 **FastAPI** (for backend API)
- 🌐 **Streamlit** (for frontend interface)
- 🐬 **MySQL** (as the database)

## 🧩 Features
- Search MeSH terms by prefix
- Frontend made with Streamlit
- Backend powered by FastAPI
- MySQL database integration

## 🛠 How to Run

### 1. Start MySQL and import `mesh_db`
Make sure your MySQL database is running with a table called `mesh_terms_2`.

### 2. Run FastAPI backend
```bash
uvicorn main:app --reload
