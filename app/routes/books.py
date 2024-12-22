from fastapi import APIRouter
from app.db import books, book_id_counter
from app.models import Book

router = APIRouter()

@router.get("/")
def list_books():
    return books

@router.post("/")
def create_book(book: Book):
    global book_id_counter
    book.id = book_id_counter
    book_id_counter += 1
    books.append(book.model_dump())
    return book
