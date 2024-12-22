from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

class Book(BaseModel):
    id: int
    title: str
    author: str
    is_available: bool = True
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None  # ID is now optional for creation
    name: str
    email: str
    is_active: bool = True


class Book(BaseModel):
    id: Optional[int] = None  # ID is now optional for creation
    title: str
    author: str
    is_available: bool = True


class BorrowRecord(BaseModel):
    id: Optional[int] = None  # ID is now optional for creation
    user_id: int
    book_id: int
    borrow_date: str
    return_date: Optional[str] = None

class BorrowRecord(BaseModel):
    id: int
    user_id: int
    book_id: int
    borrow_date: str
    return_date: Optional[str] = None
