from fastapi import APIRouter
from app.db import borrow_records, borrow_id_counter
from app.models import BorrowRecord

router = APIRouter()

@router.get("/")
def list_borrow_records():
    return borrow_records

@router.post("/")
def create_borrow_record(record: BorrowRecord):
    global borrow_id_counter
    record.id = borrow_id_counter
    borrow_id_counter += 1
    borrow_records.append(record.model_dump())
    return record
