from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI(title="FastAPI Assignment: Items API")


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True


# In-memory storage for the assignment (replace with DB in real apps)
items: Dict[int, Item] = {}
next_id = 1


@app.get("/items")
def list_items():
    return {item_id: item.dict() for item_id, item in items.items()}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    item_id = next_id
    items[item_id] = item
    next_id += 1
    return {"id": item_id, **item.dict()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"id": item_id, **item.dict()}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return None


# Helpful note for students:
# - Expand validation rules in the Item model
# - Add query parameters for filtering and pagination
# - Add tests using httpx or requests
