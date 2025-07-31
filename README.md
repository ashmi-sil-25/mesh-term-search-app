# 🔍 MeSH Term Search App

A Medical Subject Headings (MeSH) term search tool built using:
- 🚀 **FastAPI** (backend API)
- 🌐 **Streamlit** (frontend UI)
- 🐬 **MySQL** (database)

---

## 🧩 Features

- 🔎 Search MeSH terms using prefix-based input
- ⚡ FastAPI for efficient backend APIs
- 💻 Streamlit for an intuitive web interface
- 🐬 MySQL integration for storing MeSH data
- 🔄 Handles both descriptors and entry terms

---

## 🛠️ How to Run

1. Start MySQL and Import the Database

Make sure MySQL is installed and running.

```sql
CREATE DATABASE mesh_db;

USE mesh_db;

CREATE TABLE mesh_terms_2 (
    DescriptorName VARCHAR(255),
    Synonyms VARCHAR(255)
);
➡️ How to get data:
Download from the official MeSH site:
🔗 https://www.nlm.nih.gov/mesh/meshhome.html
(Recommended file: desc2024.xml or latest)

2. Install Dependencies
(Optional but recommended) Create a virtual environment:
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

Install all Python requirements:
pip install -r requirements.txt

3. Run the FastAPI Backend
In one terminal:
uvicorn main:app --reload
API root: http://127.0.0.1:8000/

Swagger docs: http://127.0.0.1:8000/docs

4. Run the Streamlit Frontend
In another terminal:
streamlit run app.py
Opens on: http://localhost:8501

🧬 Database Source (MeSH)
To use the app, your MySQL table mesh_terms_2 should contain:
DescriptorName	Synonyms
Cardiovascular Agents	Cardio Drugs
Cardiology	Heart Medicine

🔄 Optional: Convert XML to CSV
You may use a Python script to extract DescriptorName and Synonyms from desc2024.xml.

📦 Import CSV into MySQL
LOAD DATA INFILE 'path/to/your/mesh_terms.csv'
INTO TABLE mesh_terms_2
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

💬 Example API Request
Endpoint:
GET /search?term=cardio

Response:
[
  {"term": "Cardiovascular Agents", "type": "Descriptor"},
  {"term": "Cardio Drugs", "type": "EntryTerm"}
]

🧰 Tech Stack
FastAPI — for backend APIs
Streamlit — for frontend UI
MySQL — relational database
Uvicorn — ASGI server for FastAPI

🙋‍♀️ Author
Made with ❤️ by Ashmi Sil

CSE Student | Project-based Learner | Loves clean UI and meaningful tech

🌟 Contributions & Feedback
Have ideas? Found a bug?
Fork the repo, raise an issue, or submit a pull request!

🪪 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it with proper attribution.


