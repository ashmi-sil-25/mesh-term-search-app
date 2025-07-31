"""FastAPI backend for searching MeSH terms from a MySQL database."""

from typing import List, Dict
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import mysql.connector.errors as db_errors

app = FastAPI()

# Allow frontend to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (can be restricted in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db_connection():
    """Establish a connection to the MySQL database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",        # Replace with your MySQL username
        password="1234",    # Replace with your MySQL password
        database="mesh_db"  # Replace with your MySQL database name
    )


@app.get("/")
def home():
    """Home route for API health check."""
    return {"message": "Welcome to MeSH Search API"}


@app.get("/search", response_model=List[Dict])
def search_mesh(term: str = Query(..., min_length=1)):
    """
    Search MeSH terms based on a prefix string.

    Args:
        term (str): The search term entered by the user.

    Returns:
        List[Dict]: A list of matching terms and their types.
    """
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            SELECT DescriptorName AS term, 'Descriptor' AS type
            FROM mesh_terms_2
            WHERE LOWER(DescriptorName) LIKE %s
            UNION
            SELECT Synonyms AS term, 'EntryTerm' AS type
            FROM mesh_terms_2
            WHERE Synonyms IS NOT NULL AND LOWER(Synonyms) LIKE %s
            LIMIT 10;
        """
        prefix = term.lower() + "%"
        cursor.execute(query, (prefix, prefix))
        results = cursor.fetchall()

        return [{"term": row[0], "type": row[1]} for row in results]

    except db_errors.Error as db_err:
        return [{"term": f"Database error: {str(db_err)}", "type": "Error"}]

    except Exception as err:
        return [{"term": f"Unexpected error: {str(err)}", "type": "Error"}]

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

#uvicorn main:app --reload