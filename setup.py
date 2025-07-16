from fastapi import FastAPI

app = FastAPI(
    title="Route Me Up API",
    description="A simple FastAPI application with multiple endpoints.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/echo")
def echo(data: dict):
    return {"received": data}