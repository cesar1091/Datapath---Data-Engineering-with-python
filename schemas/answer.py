from datetime import date
from pydantic import BaseModel


class Answer1(BaseModel):
    department_name: str
    order_item_subtotal: float

class Answer2(BaseModel):
    category_name: str
    order_item_quantity: str

class Answer3(BaseModel):
    customer_id: str
    customer_fname: str
    customer_lname: str
    order_item_quantity: str

class Answer4(BaseModel):
    order_date: date
    order_item_quantity: str