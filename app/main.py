from fastapi import FastAPI
from app.routes import users, books, borrow

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the E-Library API!"}


app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(borrow.router, prefix="/borrow", tags=["Borrow"])
