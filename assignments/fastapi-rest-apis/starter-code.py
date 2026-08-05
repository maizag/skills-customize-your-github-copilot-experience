from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST API Assignment")


class Item(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., ge=0)
    in_stock: bool = True


# Simula um banco de dados em memoria.
items_db: dict[int, Item] = {}


@app.get("/")
def read_root():
    return {"status": "ok", "message": "FastAPI server running"}


@app.post("/items", status_code=201)
def create_item(item: Item):
    if item.id in items_db:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items_db[item.id] = item
    return item


@app.get("/items")
def list_items():
    return list(items_db.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    if updated_item.id != item_id:
        raise HTTPException(status_code=400, detail="Path ID and body ID must match")
    items_db[item_id] = updated_item
    return updated_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items_db.pop(item_id)
    return {"deleted": deleted_item.id}


# Execute com:
# uvicorn starter-code:app --reload
