import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.get("/items/{item_id}/{user_name}")
def read_item(item_id: int, user_name: str):
    return {"item_id": item_id, "user_name": user_name}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
