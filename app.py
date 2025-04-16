from fastapi import FastAPI
import httpx
import pyodbc

app = FastAPI()


server = 'webappsql-server.database.windows.net'
database = 'webappdb'
username = 'yourusername'   # <-- replace with your DB username
password = 'yourpassword'   # <-- replace with your DB password
driver = '{ODBC Driver 17 for SQL Server}'

def get_connection():
    try:
        conn = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        )
        return conn
    except Exception as e:
        print("Error connecting to DB:", e)
        return None

@app.get("/")
def read_root():
    return {"message": "Hello from Azure Web Service! Modus ETP"}

@app.get("/external")
async def call_external_api():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.publicapis.org/entries")
        return {"api_count": len(response.json()["entries"])}

@app.get("/users")
def read_users():
    conn = get_connection()
    if not conn:
        return {"error": "Failed to connect to database"}
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users")  # Replace with your actual table/column
    result = [row[0] for row in cursor.fetchall()]
    return {"users": result}
