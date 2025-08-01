from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str
    is_done: bool = False

items = []



@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# uvicorn main:app --reload
# curl -X POST -H "Content-Type: application/json" -d '{"text": "Buy milk"}' http://127.0.0.1:8000/items
# curl -X GET http://127.0.0.1:8000/items/0
# add /docs to end of url to open Swagger UI(interactive documentation tool for API testing and development)