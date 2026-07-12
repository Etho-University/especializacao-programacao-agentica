from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    category: str
    stock: int = 0

def get_db():
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.post("/products")
def create_product(product: Product):
    db = get_db()
    # PROBLEMA: SQL injection — product.name interpolado direto
    query = f"INSERT INTO products (name, price, category, stock) VALUES ('{product.name}', {product.price}, '{product.category}', {product.stock})"
    db.execute(query)
    db.commit()
    return {"status": "created"}

@app.get("/products")
def list_products(category: Optional[str] = None):
    db = get_db()
    if category:
        results = db.execute(f"SELECT * FROM products WHERE category = '{category}'").fetchall()
    else:
        results = db.execute("SELECT * FROM products").fetchall()
    return {"products": [dict(r) for r in results]}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    db = get_db()
    # PROBLEMA: não verifica se o produto existe antes de deletar
    db.execute(f"DELETE FROM products WHERE id = {product_id}")
    db.commit()
    return {"status": "deleted"}

@app.get("/products/search")
def search_products(q: str):
    db = get_db()
    # PROBLEMA: busca sem índice, vai fazer full table scan
    results = db.execute(f"SELECT * FROM products WHERE name LIKE '%{q}%'").fetchall()
    return {"results": [dict(r) for r in results]}
