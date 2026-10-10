# Main entry point 

from fastapi import FastAPI
from app.api.router import router as api_router

app = FastAPI()

app.include_router(api_router)


@app.get("/")
def root():
    return "Hellow from fastapi"


@app.get("/greet")
def greet(name):
    return {"message": f"Hellow, unknown"}


@app.get("/greet/{name}")
def greet_user(name: str, greeting: str | None = "Hellow"):
    return {"message": f"{greeting} {name}"}
