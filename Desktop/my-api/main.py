from fastapi import FastAPI
from database import get_db, init_db

app = FastAPI()

# Create table when API starts
init_db()

@app.get("/")
def home():
    return {"message": "Level 3 API with Database!"}

@app.post("/items/")
def add_item(name: str):
    conn = get_db()
    conn.execute("INSERT INTO items (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return {"added": name}

@app.get("/items/")
def list_items():
    conn = get_db()
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return {"items": [dict(item) for item in items]}