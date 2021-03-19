from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "HelloWorld"}


@app.get("/items/{item_id}/{user_name}")
def read_item(item_id: int, user_name: str):
    return {"item_id": item_id, "user_name": user_name}
