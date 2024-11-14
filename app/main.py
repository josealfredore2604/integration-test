from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Hello, World!"}

@app.get("/db-status")
def db_status():
  try:
    conn = psycopg2.connect(
      dbname="testdb",
      user="testuser",
      password="testpass",
      host="db",
      port=5432
    )
    conn.close()
    return {"status": "Database is reachable"}
  except Exception as e:
    return {"status": "Error", "details": str(e)}
